from utils.evaluator import Evaluator
import time

def main(path:str):
    start_time = time.time()

    eval = Evaluator(path)
    eval.execute()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tempo de execução: {execution_time*1000:.1f} ms")

if __name__ == "__main__":
    path:str = "io/input.txt"
    main(path)
