# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'variables': {
      'version_py_path': '<(DEPTH)/chromium/build/util/version.py',
      'version_path': '<(DEPTH)/chromium/chrome/VERSION',
    },
    'version_py_path': '<(version_py_path)',
    'version_path': '<(version_path)',
    'version_full':
        '<!(python <(version_py_path) -f <(version_path) -t "@MAJOR@.@MINOR@.@BUILD@.@PATCH@")',
    'version_libchrome_short':
        '<!(python <(version_py_path) -f <(version_path) -t "@BUILD@.@PATCH@")',
    'version_mac_dylib':
        '<!(python <(version_py_path) -f <(version_path) -t "@BUILD@.@PATCH_HI@.@PATCH_LO@" -e "PATCH_HI=int(PATCH)/256" -e "PATCH_LO=int(PATCH)%256")',
  },  # variables
}
