# SPDX-License-Identifier: MIT
# Copyright (c) 2022, Mathias Laurin

import enum
from typing import FrozenSet, Optional, Tuple

def get_supported_ciphers() -> FrozenSet[bytes]: ...

class Mode(enum.Enum):
    ECB: int
    CBC: int
    CFB: int
    OFB: int
    CTR: int
    GCM: int
    STREAM: int
    CCM: int
    XTS: int
    CHACHAPOLY: int

class Cipher:
    def __init__(
        self, cipher_name: bytes, key: bytes, mode: Mode, iv: Optional[bytes]
    ) -> None: ...
    def __str__(self) -> str: ...
    @property
    def block_size(self) -> int: ...
    @property
    def mode(self) -> Mode: ...
    @property
    def iv_size(self) -> int: ...
    @property
    def _type(self) -> bytes: ...
    @property
    def name(self) -> bytes: ...
    @property
    def key_size(self) -> int: ...
    def encrypt(self, message: bytes) -> bytes: ...
    def decrypt(self, message: bytes) -> bytes: ...

class AEADCipher:
    def __init__(
        self,
        cipher_name: bytes,
        key: bytes,
        mode: Mode,
        iv: Optional[bytes],
        ad: Optional[bytes],
    ) -> None: ...
    def __str__(self) -> str: ...
    @property
    def block_size(self) -> int: ...
    @property
    def mode(self) -> Mode: ...
    @property
    def iv_size(self) -> int: ...
    @property
    def _type(self) -> bytes: ...
    @property
    def name(self) -> bytes: ...
    @property
    def key_size(self) -> int: ...
    def encrypt(self, message: bytes) -> Tuple[bytes, bytes]: ...
    def decrypt(self, message: bytes, tag: bytes) -> bytes: ...
