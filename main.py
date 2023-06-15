"""
Build system.

Usage:
  main.py <command> <argument>
  main.py <command> <argument> <name>

Examples:
  main.py list builds
  main.py list tasks
  main.py get builds <build_name>
  main.py get task <task_name>

Options:
  -h, --help

"""
from docopt import docopt
import yaml

def read_yaml(path_build, path_tasks):
    with open(path_build) as build_file, open(path_tasks) as tasks_file:
        build_list = yaml.load(build_file, Loader=yaml.FullLoader)
        tasks_list = yaml.load(tasks_file, Loader=yaml.FullLoader)
    return build_list, tasks_list

def list_data(name_dict):
    task_or_build = argument
    for build in range(len(name_dict[task_or_build])):
        print('* '+ name_dict[task_or_build][build]['name'])

def get_data(get_dict, name, mode):
    findFlag = 0

    for task in get_dict['tasks']:
        if name in task['name']:
            findFlag = 1
            dependencies_first = list(dep for dep in task['dependencies'])

            if mode == 'task':
                dep_str = ', '.join(dependencies_first)
                return dep_str
            
            if dependencies_first != []:
                dependencies_second = []
                for task in dependencies_first:
                    if task != None:
                        results = get_data(get_dict, task, 'build')
                        if results != None:
                            for el in results:
                                dependencies_second.append(el)
                        
            else: return

            results = ([dependencies_first, dependencies_second] if dependencies_second != [] else dependencies_first)

            break
           
    if findFlag == 0:
        print(f"{name} task doesn't exist")
        return
    return results

def get_data_build(get_dict, tasks_dict, name):
    findFlag = 0
    
    for el in get_dict['builds']:
        if name in el['name']:
            findFlag = 1

            tasks = list(dep for dep in el['tasks'])
            result_lst = tasks[:]

            for task in tasks:
                dependencies = get_data(tasks_dict, task, 'build')
                if dependencies != None:
                    for lst in dependencies:
                        for el in lst:
                            result_lst.append(el)

            result_lst.reverse()
            task_str = ', '.join(result_lst)
            return task_str
        
    if findFlag == 0:
        return f"{name} build doesn't exist"


if __name__ == '__main__':
    args = docopt(__doc__)

    path_build = 'builds.yaml'
    path_tasks = 'tasks.yaml'

    command = args['<command>']
    argument = args['<argument>']
    name = args['<name>']

    build_dict, task_dict = read_yaml(path_build, path_tasks)

    if command == 'list':
        if argument == 'builds':
            print("List of available builds:")
            build_list = list_data(build_dict)
        elif argument == 'tasks':
            print("List of available tasks:")
            tasks_list = list_data(task_dict)
    
    if command == 'get':
        if argument == 'build':
            print("Build info:")
            results = get_data_build(build_dict, task_dict, name)
        elif argument == 'task':
            print("Task info:")
            results = get_data(task_dict, name, 'task')

        print(f"* name: {name}")
        print(f"* {'tasks: ' if argument == 'build' else 'dependencies: '} {results}")
