import mlflow

if __name__ == "__main__":
    mlflow.run(uri='https://github.com/raphael-bos/mlflow.git', entry_point='train.py', use_conda=False)