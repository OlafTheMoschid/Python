import graph
import pytest

graph = graph.Graph()

graph.addEdge('Мариинск', 'Яя', 139)
graph.addEdge('Мариинск', 'Юрга', 261)
graph.addEdge('Мариинск', 'Яшкино', 240)

graph.addEdge('Яя', 'Юрга', 163)
graph.addEdge('Яя', 'Анжеро-Судженск', 33)

graph.addEdge('Яшкино', 'Юрга', 43)
graph.addEdge('Юрга', 'Анжеро-Судженск', 133)
graph.addEdge('Юрга', 'Кемерово', 97)

graph.addEdge('Анжеро-Судженск', 'Кемерово', 99)
graph.addEdge('Яшкино', 'Томск', 146)

graph.addEdge('Юрга', 'Томск', 106)
graph.addEdge('Томск', 'Кемерово', 216)


def func(start, end):
    dist, path = graph.dijkstra(start)
    path.append(end)

    for key, value in dist.items():
        if key == end:
            v = value
            break

    if v != 10 ** 6:
        print('Минимальный путь от города', start, 'до города',
              end, '=', value, 'км\nПолученный путь: ')
        print(*path, sep=' -> ')
        return value
    else:
        print('Пути не существует')
        return None


def test_no_entry_city():
    start = 'Анжеро-Судженск'
    end = 'Мариинск'
    assert func(start, end) == None


def test_no_wayout_city():
    start = 'Кемерово'
    end = 'Мариинск'
    assert func(start, end) == None


def test_no_path_city():
    start = 'Яшкино'
    end = 'Яя'
    assert func(start, end) == None


def test_single_city():
    start = 'Яшкино'
    end = 'Яшкино'
    assert func(start, end) == 0


def test_usual_path():
    start = 'Яшкино'
    end = 'Кемерово'
    assert func(start, end) == 140
