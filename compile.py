#!/usr/bin/env python3

# import required module
import os
import itertools
# assign directory
directory = 'src/themes'

highlights = ''

with open(os.path.join('src', 'template-nvchad.toml'), "r") as text_file:
    for line in itertools.islice(text_file, 7, 366):
        highlights += line

if not os.path.exists('templates'):
    os.mkdir('templates')

if not os.path.exists('compiled'):
    os.mkdir('compiled')

os.system('rm -r lua')
os.system('rm -r colors')

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        themename = filename.split('.')[0].replace('-', '_')
        palette = ''
        bg = 'dark'
        with open(f, "r") as text_file:
            lines = text_file.readlines()
            started = False
            brackets = 0
            for line in lines:
                if started:
                    if '}' in line:
                        brackets += 1
                    line = line.replace("--", "#").replace(",", "").replace(
                        '{', '').replace('}', '').replace('M.base_16 =', '').strip()
                    if len(line) > 0:
                        palette += line + '\n'
                    if brackets >= 2:
                        started = False
                if line.startswith('M.base_30 = {'):
                    started = True
                if line.startswith('vim.opt.bg') and 'light' in line:
                    bg = 'light'
        template_path = "templates/" + themename + ".toml"
        with open(template_path, "w") as toml:
            toml.write("[information]\n")
            toml.write('name="' + themename + '"\n')
            toml.write('author="Ken Zhou <kendotzhou@gmail.com>"\n')
            toml.write('background="'+bg+'"\n')
            toml.write('\n')
            toml.write('[palette]\n')
            toml.write(palette)
            toml.write('\n')
            toml.write(highlights)
        print('compiling ' + template_path)
        os.system("cd compiled && colorgen-nvim ../" + template_path)
        os.system('cp -r compiled/' + themename + '/colors .')
        os.system('cp -r compiled/' + themename + '/lua .')

os.system('rm -r compiled')
