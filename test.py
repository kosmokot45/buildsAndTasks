# pytest test.py::test_get_data_build
# pytest test.py::test_get_data

from main import read_yaml, list_data, get_data, get_data_build

def test_get_data():
    build_dict, task_dict = read_yaml('builds.yaml', 'tasks.yaml')
    name = 'upgrade_lime_leprechauns'
    result_good = 'bring_black_leprechauns, build_blue_leprechauns, write_lime_leprechauns'
    assert get_data(task_dict, name, 'task') == result_good

def test_get_data_build_1():
    build_dict, task_dict = read_yaml('builds.yaml', 'tasks.yaml')
    name = 'approach_important'
    result = 'upgrade_blue_centaurs, design_black_centaurs, train_silver_centaurs, read_purple_centaurs, map_gray_centaurs'
    assert get_data_build(build_dict, task_dict, name) == result

def test_get_data_build_2():
    build_dict, task_dict = read_yaml('builds.yaml', 'tasks.yaml')
    name = 'audience_stand'
    result = 'upgrade_olive_gnomes, read_blue_witches, enable_fuchsia_fairies'
    assert get_data_build(build_dict, task_dict, name) == result

def test_get_data_build_3():
    build_dict, task_dict = read_yaml('builds.yaml', 'tasks.yaml')
    name = 'time_alone'
    result = 'write_aqua_leprechauns, upgrade_olive_leprechauns, bring_purple_leprechauns, write_lime_leprechauns, build_blue_leprechauns, bring_black_leprechauns, map_black_cyclops, create_white_cyclops, build_lime_cyclops, bring_yellow_cyclops, train_white_cyclops, read_aqua_cyclops, enable_yellow_cyclops, design_silver_cyclops, bring_green_cyclops, read_lime_cyclops, enable_white_cyclops, bring_gray_cyclops, design_teal_cyclops, create_green_cyclops, coloring_green_cyclops, upgrade_lime_leprechauns, design_olive_cyclops'
    assert get_data_build(build_dict, task_dict, name) == result

def test_get_data_task_2():
    build_dict, task_dict = read_yaml('builds.yaml', 'tasks.yaml')
    name = 'write_lime_leprechauns'
    result = 'upgrade_olive_leprechauns, write_aqua_leprechauns'
    assert get_data(task_dict, name, 'task') == result

def test_get_data_build_unknow():
    build_dict, task_dict = read_yaml('builds.yaml', 'tasks.yaml')
    name = 'UNKNOWN BUILD'
    result_good = 'UNKNOWN BUILD build doesn\'t exist'
    assert get_data_build(build_dict, task_dict, name) == result_good