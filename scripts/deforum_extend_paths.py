# 'Deforum' plugin for Automatic1111's Stable Diffusion WebUI.
# Copyright (C) 2023 Artem Khrapov (kabachuha) and Deforum team listed in AUTHORS.md
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# Contact the dev team: https://discord.gg/deforum

import os
import sys

def deforum_sys_extend():
    deforum_folder_name = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-2])

    basedirs = [os.getcwd()]
    if 'google.colab' in sys.modules:
        basedirs.append('/content/gdrive/MyDrive/sd/stable-diffusion-webui') # for TheLastBen's colab
    for basedir in basedirs:
        deforum_paths_to_ensure = [
            os.path.join(deforum_folder_name, 'scripts'),
            os.path.join(deforum_folder_name, 'scripts', 'deforum_helpers', 'src')
            ]
        for deforum_scripts_path_fix in deforum_paths_to_ensure:
            if not deforum_scripts_path_fix in sys.path:
                sys.path.extend([deforum_scripts_path_fix])