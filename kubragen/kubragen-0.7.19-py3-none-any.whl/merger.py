import deepmerge

from .private.merger import option_check_key_exist, option_merge_fallback, option_type_conflict

MergerNoCreate = deepmerge.Merger(
    [
        (list, "append"),
        (dict, [option_check_key_exist, "merge"]),
    ],
    [option_merge_fallback], [option_type_conflict]
)
"""A dict/list merger that doesn't allow dict key creation, based on the :mod:`deepmerge` module."""

# A merger that allows key creation
Merger = deepmerge.Merger(
    [
        (list, "append"),
        (dict, "merge"),
    ],
    [option_merge_fallback], [option_type_conflict]
)
"""A dict/list merger, based on the :mod:`deepmerge` module."""
