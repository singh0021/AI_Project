import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ('Usage: python TaskExecution.py')
        sys.exit(0)

    # Processing command line arguments
    method = sys.argv[1]
    board = [int(i) for i in sys.argv[2].split(",")]

    print('method= ' + method )
    print(board)