from concurrent.futures import ThreadPoolExecutor, wait
from os import getcwd
import git
import argparse
from rich import print
from rich.padding import Padding
from bossman import Bossman
from bossman.resources import ResourceABC

def init(subparsers: argparse._SubParsersAction):
  parser = subparsers.add_parser("apply", help="apply local changes to remotes")
  parser.add_argument("--force", action="store_true", default=False, help="don't skip dirty resources")
  parser.add_argument("glob", nargs="?", default="*", help="select resources by glob pattern")
  parser.set_defaults(func=exec)

def exec(bossman: Bossman, glob, force=False, **kwargs):
  resources = bossman.get_resources(glob=glob)
  futures = []
  with ThreadPoolExecutor(10, "apply") as executor:
    for resource in resources:
      futures.append(executor.submit(apply_changes, bossman, resource, force))
  wait(futures)
  print(":cookie: [green]all resources up to date[green]")

def apply_changes(bossman: Bossman, resource: ResourceABC, force: bool):
  status = bossman.get_resource_status(resource)
  revisions = bossman.get_missing_revisions(resource)
  todo = len(revisions)
  if todo > 0:
    if status.dirty and not force:
      print(":stop_sign:", resource, "[magenta]dirty, skipping[/magenta]")
      return
    results = []
    for revision in revisions:
      try:
        results.append(bossman.apply_change(resource, revision))
      except RuntimeError as e:
        if not force:
          raise e
        results.append(":exclamation_mark: {} an error occurred while applying {}\n{}", resource, revision, e)
    for idx, result in enumerate(results):
      print("{}/{}".format(idx+1, todo), result)
  else:
    print(":white_check_mark:", resource, "is up to date")