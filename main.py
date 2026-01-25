from cli import parse_args
from modes import interactive_mode, args_mode

def main():
    args = parse_args()

    if args.from_currency and args.to_currency and args.amount:
        args_mode(args)

    else:
        interactive_mode()


if __name__ == "__main__":
    main()