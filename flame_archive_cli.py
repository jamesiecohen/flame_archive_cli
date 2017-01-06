#!/usr/bin/python
import os
import platform

## run "/usr/discreet/io/bin/flame_archive -l" to get a list of projects.
## copy and paste the exact text of the project here
flame_project = '3645_verizon_reset'

flame_archive = '/usr/discreet/io/bin/flame_archive'
## this assumes you have an external drive at this path
disk_root = '/media/archive'
computer_name = platform.node()
archive_name = '{}-{}'.format(flame_project, computer_name)
archive_base_dir = '{}_{}'.format(computer_name, 'archive')
archive_base_dir = os.path.join(disk_root, archive_base_dir)
archive_path = os.path.join(disk_root, archive_base_dir, archive_name)
initalize_command = '{} -f -F {} -i 50'.format(flame_archive, archive_path)
archive_command = '{} -a -P {} -F {} -v'.format(flame_archive, flame_project, archive_path)

print "#This is the command to initialize a new archive for your project."
print initalize_command

print ""
print "#This is the command to run your archive."
print archive_command
