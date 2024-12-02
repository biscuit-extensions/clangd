from __future__ import annotations

import typing

from .clangd import clangd

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


def setup(api: ExtensionsAPI) -> None:
    api.register("clangd", clangd(api))
