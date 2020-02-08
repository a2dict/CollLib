import hashlib
from typing import Dict, List


class CollKeys(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    def select_keys(self, d: Dict, ks: List) -> Dict:
        return {k: v
                for k, v in d.items()
                if k in ks}

    def exclude_keys(self, d: Dict, ks: List) -> Dict:
        return {k: v
                for k, v in d.items()
                if k not in ks}

    def merge(self, d1: Dict, d2: Dict) -> Dict:
        return {**d1, **d2}

    def exclude_empty(self, d: Dict) -> Dict:
        return {k: v
                for k, v in d.items()
                if v is not None and v != ""}

    def md5_str(self, s: str) -> str:
        bs = s.encode('utf8')
        return hashlib.md5(bs).hexdigest()

    def get_sign_content(self, d: Dict) -> str:
        return '&'.join(['{}={}'.format(k, v) for k, v in sorted(d.items())])
