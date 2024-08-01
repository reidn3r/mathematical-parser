from utils.evaluator import Evaluator

def main(path:str):
    eval = Evaluator(path)
    eval.execute()


if __name__ == "__main__":
    path:str = "../io/input.txt"
    main(path)
