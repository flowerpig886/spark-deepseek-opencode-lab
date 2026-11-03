# SPDX-License-Identifier: MIT
# Copyright (c) 2026 flowerpig886
"""Prepare a fixed-version single-lane cache source file; never alter the input."""
import argparse,ast,hashlib
from pathlib import Path
ORIGINAL='f726784419face244928df9d69236163135da5cafde11613304e7187fa7a401b'
PATCHED='38b14bea1eeb2d6a454d0a1166cc8abe70a928d2a5be5c9399a58e8265745c72'
OLD=b'self.concurrent = int(parallel) > 1'
NEW=b'self.concurrent = int(parallel) > 1 or (int(parallel) == 1 and os.environ.get("TF_DS_SINGLE_LANE_CACHE", "0") == "1")'
def prepare(source):
 if hashlib.sha256(source).hexdigest()!=ORIGINAL:raise ValueError('Original source SHA256 mismatch; use the recorded version, do not force-patch.')
 if source.count(OLD)!=1:raise ValueError('Expected exactly one original scheduler condition.')
 result=source.replace(OLD,NEW)
 ast.parse(result.decode('utf-8'))
 if hashlib.sha256(result).hexdigest()!=PATCHED:raise ValueError('Patched source SHA256 mismatch.')
 return result
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);p.add_argument('output',type=Path);args=p.parse_args()
 if args.input.resolve()==args.output.resolve():p.error('Input and output must differ; preserve original source.')
 if args.output.exists():p.error('Output already exists; inspect it instead of overwriting.')
 result=prepare(args.input.read_bytes());args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_bytes(result)
 print('Prepared fixed-version engine.py; SHA256 '+PATCHED+'. No image built or service changed.')
if __name__=='__main__':main()
