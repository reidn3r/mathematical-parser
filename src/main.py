from utils.exec_class import execution

def main(path:str):
    exec_class = execution(path)
    exec_class.exec()


if __name__ == "__main__":
    path:str = "io/input.txt"
    main(path)