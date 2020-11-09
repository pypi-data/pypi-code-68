#!/usr/bin/env python

from utz import *

from .version import get_version
version = get_version()

DEFAULT_IMAGE = f'runsascoded/gsmo:{version}'
DEFAULT_DIND_IMAGE = f'{DEFAULT_IMAGE}:dind_{version}'

from .cli import Arg, run_args, load_run_config
from .config import clean_group, clean_mount, lists, Config, DEFAULT_SRC_MOUNT_DIR, DEFAULT_RUN_NB

def main():
    parser = ArgumentParser()
    parser.add_argument('input',nargs='?',help='Input directory containing run.ipynb (and optionally gsmo.yml, or other path specified by "-y"); defaults to current directory')

    jupyter_args = [
        Arg('-d','--detach',action='store_true',help="When booting into Jupyter server mode, detach the container"),
        Arg('-D','--no-docker',dest='docker',default=True,action='store_false',help="Run in the current shell instead of in Docker"),
        Arg('-O','--no-open',action='store_true',help='Skip opening Jupyter notebook server in browser'),
        Arg('-s','--shell',action='store_true',help="Open a /bin/bash shell in the container (instead of running a jupyter server)"),  # TODO: implement
    ]

    docker_args = [
        Arg('-a','--apt',help='Comma-separated list of packages to apt-get install'),
        Arg('-b','--build-arg',nargs='*',help='Comma-separated list of packages to apt-get install'),
        Arg('--dind',action='store_true',help="When set, mount /var/run/docker.sock in container (and default to a base image that contains docker installed)"),
        Arg('--dst',help='Path inside Docker container to mount current directory/repo to (default: /src)'),
        Arg('-e','--env',nargs='*',help='Environment variables to pass to Docker container'),
        Arg('-E','--env-file',help="File with environment variables to pass to Docker container"),
        Arg('-i','--image',help=f'Base docker image to build on (default: f{DEFAULT_IMAGE})'),
        Arg('-I','--no-interactive',action='store_true',help="Don't run interactively / allocate a TTY (i.e. skip `-it` flags to `docker run`)"),
        Arg('-g','--image-group',action='store_true',help='Create current group inside Docker image (at build time)'),
        Arg('-G','--group',nargs='*',help='Groups to add user to when running the Docker container'),
        Arg('-n','--name',help='Container name (defaults to directory basename)'),
        Arg('-p','--pip',help='Comma-separated (or multi-arg) list of packages to pip install'),
        Arg('-P','--port',nargs='*',help='Ports (or ranges) to expose from the container (if Jupyter server is being run, the first port in the first provided range will be used); can be passed multiple times and/or as comma-delimited lists'),
        Arg('--rm','--remove-container',action='store_true',help="Remove Docker container after run (pass `--rm` to `docker run`)"),
        Arg('-R','--skip-requirements-txt',action='store_true',help="Skip {reading,`pip install`ing} any requirements.txt that is present"),
        Arg('--sudo',action='store_true',help="Ensure Docker image user has sudo privileges"),
        Arg('-t','--tag',help='Comma-separated (or multi-arg) list of tags to add to built docker image'),
        Arg('-u','--image-user',action='store_true',help="Create current user inside Docker image (at build time)"),
        Arg('-U','--root','--no-user',action='store_true',help="Run docker as root (instead of as the current system user)"),
        Arg('-v','--mount',nargs='*',help='Paths to mount into Docker container; relative paths are accepted, and the destination can be omitted if it matches the src (relative to the current directory, e.g. "home" → "/home")'),
        Arg('--missing-mounts',default='raise',choices=['raise','err','error','warn','ignore','ok',],help='Control behavior when any mount paths are nonexistent'),
        Arg('--pip_mount',help='Optionally `pip install -e` a mounted directory inside the container before running the usual entrypoint script'),
    ]

    subparsers = parser.add_subparsers()

    jupyter_parser = subparsers.add_parser('jupyter', help='Boot (and attempt to open in browser) a Jupyter server running in a Docker image built for this module', aliases=['j'])
    jupyter_parser.set_defaults(cmd='jupyter')

    run_parser = subparsers.add_parser('run', help='Run this module in a purpose-built Docker image', aliases=['r'])
    run_parser.set_defaults(cmd='run')

    shell_parser = subparsers.add_parser('shell', help='Boot a Bash shell in a Docker image built for this module', aliases=['sh','s','bash'])
    shell_parser.set_defaults(cmd='shell')

    for arg in docker_args:
        parser.add_argument(*arg.args, **arg.kwargs)

    for arg in jupyter_args:
        jupyter_parser.add_argument(*arg.args, **arg.kwargs)

    for arg in run_args:
        run_parser.add_argument(*arg.args, **arg.kwargs)

    args = parser.parse_args()
    jupyter_mode = shell_mode = run_mode = False
    print(f'args: {args}')
    cmd = getattr(args, 'cmd', None)
    if cmd =='jupyter':
        jupyter_mode = True
    elif cmd == 'shell':
        shell_mode = True
    elif cmd == 'run':
        run_mode = True
    else:
        raise ValueError(f'Unknown cmd: {cmd}')

    config = Config(args)
    get = partial(Config.get, config)


    if run_mode:
        run_config = load_run_config(args)

        dir = args.dir
        if dir:
            print(f'Running in: {dir}')
            chdir(dir)


    cwd = getcwd()
    input = args.input or cwd


    dst = get('dst',DEFAULT_SRC_MOUNT_DIR)
    src = cwd

    # Detect when we are running a git submodule, and adjust src mount to include the containing Git repository (and Git
    # directory, which will contain this module's Git dir under its .git/modules); this is necessary for Git operations
    # (specifically commits) to work as expected inside the container
    git_dir = join(src, '.git')
    if isfile(git_dir):
        with open(git_dir,'r') as f:
            [ ln ] = [ l for line in f.readlines() if (l := line.strip()) ]
        rgx = r'^gitdir: (?P<path>.*)$'
        if not (m := match(rgx, ln)):
            raise Exception(f'Unrecognized .git file contents: {ln}')
        path = m['path']
        pcs = path.split(sep)
        workdir = []
        i = 0
        while i < len(pcs) and pcs[i] == '..':
            workdir = [basename(src)] + workdir
            src = dirname(src)
            i += 1
        if i + 2 >= len(pcs) or pcs[i] != '.git' or pcs[i+1] != 'modules':
            raise Exception(f'Expected gitdir path of the form `(../)*.git/modules`; found {path}')
        print(f'workdir: {workdir}')
        workdir = join(dst, *workdir)
        print(f'Parsed ancestor mount for submodule: {src}:{dst}, workdir {workdir}')
    else:
        workdir = dst

    # Load env var configs
    envs = get('env', [])
    if isinstance(envs, (list, tuple)):
        envs = dict([
            env.split('=', 1)
            for env in envs
        ])
    elif envs is not None and not isinstance(envs, dict):
        raise ValueError(f'Unexpected env dict: {envs}')

    env_file = get('env_file')

    commit = lists(get('commit'))

    groups = lists(get('group'))
    groups = [ clean_group(group) for group in groups ]

    out = get('out') or 'nbs'

    mounts = lists(get('mount', []))
    missing_mounts = get('missing_mounts')
    mounts = [ m for mount in mounts if (m := clean_mount(mount, missing_mount=missing_mounts)) ]
    mounts += [ f'{src}:{dst}', ]

    dind = get('dind')
    if dind:
        default_image = DEFAULT_DIND_IMAGE
        mounts += [ '/var/run/docker.sock:/var/run/docker.sock']
    else:
        default_image = DEFAULT_IMAGE
    base_image = get('image', default_image)
    image = base_image

    docker = get('docker', True)
    rm = get('remove_container')

    ports = lists(get('port'))
    apts = lists(get('apt'))
    pips = lists(get('pip'))
    tags = lists(get('tag'))
    name = get('name', default=basename(input))
    skip_requirements_txt = args.skip_requirements_txt
    root = get('root')
    image_user = get('image_user')
    image_group = get('image_group')
    sudo = get('sudo')

    if jupyter_mode:
        jupyter_src_port = jupyter_dst_port = None
        jupyter_open = not args.no_open
        detach = args.detach
        shell = args.shell


    if ports:
        # Canonicalize a port argument:
        # - "5432" → "5432:5432"
        # - "8880-8890" → "8880-8890:8880-8890"
        # - "5432:5432" → "5432:5432" (no-op)
        def clean_port(port):
            pcs = port.split(':')
            if len(pcs) == 1:
                port = pcs[0]
                return f'{port}:{port}'
            elif len(pcs) == 2:
                return port
            else:
                raise ValueError(f'Unrecognized port/range: {port}')

        # Flatten and normalize comma-delimited list of port args
        ports = [
            clean_port(arg)
            for port in ports
            for arg in port.split(',')
        ]

        if jupyter_mode:
            [ src_port, dst_port ] = ports[0].split(':')

            src_pcs = src_port.split('-')
            if len(src_pcs) <= 2:
                jupyter_src_port = src_pcs[0]
            else:
                raise ValueError(f'Unrecognized port/range: {src_port}')

            dst_pcs = dst_port.split('-')
            if len(dst_pcs) <= 2:
                jupyter_dst_port = dst_pcs[0]
            else:
                raise ValueError(f'Unrecognized port/range: {dst_port}')
    else:
        if jupyter_mode:
            # Hash the module name to determine a port for Jupyter in the range [2**10,2**16)
            start = 2**10
            end = 2**16
            from hashlib import sha256
            m = sha256()
            m.update(name.encode())
            digest = int(m.hexdigest(), 16)
            jupyter_src_port = jupyter_dst_port = digest % (end-start) + start
            ports = [ f'{jupyter_src_port}:{jupyter_dst_port}', ]
        else:
            ports = []


    from .util.unix_id import UnixId
    id = UnixId()

    from utz import docker
    from utz.use import use

    file = docker.File()
    with use(file):
        # If this becomes true, write out a fresh Dockerfile (to `tmp_dockerfile`) and build an image
        # based from it; otherwise, use an extant upstream image
        build_image = False
        tmp_dockerfile = file.path

        dockerfile = join(cwd, 'Dockerfile')
        if exists(dockerfile):
            build_image = True
            copy(dockerfile, tmp_dockerfile)
        else:
            FROM(base_image)

        if apts:
            if docker:
                build_image = True
                RUN(
                    'apt-get update',
                    f'apt-get install -y {" ".join(apts)}'
                )
            else:
                stderr.write(f'Installing apt deps skipped in docker-less mode: {" ".join(apts)}\n')

        reqs_txt = join(cwd, 'requirements.txt')
        if exists(reqs_txt) and not skip_requirements_txt:
            with open(reqs_txt, 'r') as f:
                pips += [ line.rstrip('\n') for line in f.readlines() if line ]

        if pips:
            if docker:
                build_image = True
                RUN(f'pip install {" ".join(pips)}')
            else:
                import pip
                print(f'pip install {" ".join(pips)}')
                pip.main(['install'] + pips)

        if docker:
            if image_user:
                build_image = True
                RUN(f'useradd -u {id.uid} -g {id.gid} -s /bin/bash {id.user}')
            if image_group:
                build_image = True
                RUN(f'groupadd -o -g {id.gid} {id.group}')
            if sudo:
                RUN(
                    'apt-get update',
                    'apt-get install -y sudo',
                    'perl -pi -e "s/^%%sudo(.*ALL=).*/%s\\1(ALL) NOPASSWD: ALL/" /etc/sudoers' % id.user,
                )

        if build_image:
            assert docker
            file.build(name)
            image = name

    # Determine user to run as (inside Docker container)
    user_args = []
    if not root:
        uid = line('id','-u')
        if uid == '0':
            root = True
        else:
            gid = line('id','-g')
            user_args = [ '-u', f'{uid}:{gid}' ]

    # Remove any existing container
    if docker:
        if check('docker','container','inspect',name):
            run('docker','container','rm',name)

    interactive = not args.no_interactive
    if interactive:
        flags = [ '-it' ]
    else:
        flags = []
    if rm:
        assert docker
        flags += ['--rm']

    run_nb = get('run', DEFAULT_RUN_NB)

    if shell_mode:
        # Launch Bash shell
        entrypoint = '/bin/bash'
        args = []
    elif jupyter_mode:
        # Launch `jupyter notebook` server
        entrypoint = 'jupyter'
        assert jupyter_dst_port
        args = [
            'notebook',
            '--ip','0.0.0.0',
            '--port',jupyter_dst_port,
            '--ContentsManager.allow_hidden=True',
        ]
        if root:
            args += [ '--allow-root', ]
    else:
        entrypoint = 'gsmo-entrypoint'
        if not exists(run_nb):
            raise ValueError(f"Run notebook doesn't exist: {run_nb}")
        args = [ '--run', run_nb, '--out', out, ]
        if commit:
            args += [ ['--commit',path] for path in commit]


    pip_mounts = lists(get('pip_mount'))
    if pip_mounts:
        args = [ len(pip_mounts) ] + pip_mounts + [ entrypoint ] + args
        entrypoint = '/gsmo/pip_entrypoint.sh'


    if run_mode:
        RUN_CONFIG_YML_PATH = '/run_config.yml'
        if run_config:
            run_config_path = NamedTemporaryFile(delete=False)
            with open(run_config_path.name,'w') as f:
                yaml.safe_dump(dict(run_config), f)
            mounts += [ f'{run_config_path.name}:{RUN_CONFIG_YML_PATH}' ]
            args += [ '-Y',RUN_CONFIG_YML_PATH ]

    def get_git_id(k, fmt):
        try:
            v = line('git','config',f'user.{k}')
        except CalledProcessError:
            v = line('git','log','-n','1',f'--format={fmt}')
            stderr.write(f'Falling back to Git user {k} from most recent commit: {v}\n')
        return v

    # Get Git user name/email for propagating into image
    id = o(
        name  = get_git_id( 'name', '%an'),
        email = get_git_id('email', '%ae'),
    )


    # Set up author info for git committing
    envs = {
        **envs,
       'HOME': '/home',
       'GIT_AUTHOR_NAME'    : id.name,
       'GIT_AUTHOR_EMAIL'   : id.email,
       'GIT_COMMITTER_NAME' : id.name,
       'GIT_COMMITTER_EMAIL': id.email,
    }

    # Build Docker CLI args
    env_args = [ [ '-e', f'{k}={v}' ] for k, v in envs.items() ]
    if env_file: env_args += [ '--env-file', env_file ]
    mount_args = [ [ '-v', mount ] for mount in mounts ]
    port_args = [ [ '-p', port ] for port in ports ]
    group_args = [ [ '--group-add', group ] for group in groups ]
    entrypoint_args = [ '--entrypoint', entrypoint ]
    workdir_args = [ '--workdir', workdir ]

    all_args = \
        flags + \
        entrypoint_args + \
        env_args + \
        mount_args + \
        port_args + \
        user_args + \
        workdir_args + \
        group_args + \
        [image] + \
        args


    if docker:
        if jupyter_mode and check('which', 'open'):
            # 1. run docker container in detached mode
            # 2. parse+open jupyter token URL in browser (try every 1s)
            # 3. re-attach container
            run(
                'docker','run',
                '-w',dst,
                '-d',
                '--name',name,
                all_args,
            )
            while True:
                lns = lines('docker','exec',name,'jupyter','notebook','list')
                if lns[0] != 'Currently running servers:':
                    raise Exception('Unexpected `jupyter notebook list` output:\n\t%s' % "\n\t".join(lns))
                if len(lns) == 2:
                    ln = lns[1]
                    rgx = f'(?P<url>http://0\.0\.0\.0:(?P<port>\d+)/\?token=(?P<token>[0-9a-f]+)) :: {dst}'
                    if not (m := match(rgx, ln)):
                        raise RuntimeError(f'Unrecognized notebook server line: {ln}')
                    if m['port'] != str(jupyter_dst_port):
                        raise RuntimeError(f'Jupyter running on unexpected port {m["port"]} (!= {jupyter_dst_port})')
                    token = m['token']
                    url = f'http://127.0.0.1:{jupyter_src_port}?token={token}'
                    if jupyter_open:
                        run('open',url)
                    if shell:
                        run('docker','exec','-it',name,'/usr/bin/env','bash')
                    else:
                        if not detach:
                            run('docker','attach',name)
                    break
                else:
                    SLEEP_INTERVAL = 1
                    print(f'No Jupyter server found in container {name}; sleep {SLEEP_INTERVAL}s…')
                    sleep(SLEEP_INTERVAL)
        else:
            run(
                'docker','run',
                '-w',dst,
                '--name',name,
                all_args,
            )
    else:
        # if not jupyter:
        #     raise ValueError(f'In non-docker mode, only -j/--jupyter mode is supported')
        if jupyter_src_port != jupyter_dst_port:
            raise ValueError(f'Mismatching jupyter ports in non-docker mode: {jupyter_src_port} != {jupyter_dst_port}')
        jupyter_port = jupyter_src_port
        run('jupyter','notebook','--port',jupyter_port,)


if __name__ == '__main__':
    main()
