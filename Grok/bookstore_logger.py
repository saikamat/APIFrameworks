import logging, random, time, datetime

ACTIONS = ["PURCHASE", "REFUND"]
BOOK_IDS = [f"BK{n}" for n in range(100, 110)]
CUSTOMERS = ["Alice Johnson", "Bob Lee", "Chen Wu", "Dina Patel", "Evan Brooks"]

logger = logging.getLogger("bookstore")
logger.setLevel(logging.INFO)
fh = logging.FileHandler("bookstore.log")
fmt = logging.Formatter("%(message)s")
fh.setFormatter(fmt)
logger.addHandler(fh)

def log_line(action, book_id, price, customer):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f'{now} {action} book_id={book_id} price={price:.2f} customer="{customer}"'
    logger.info(line)

if __name__ == "__main__":
    print("Writing logs to bookstore.log (Ctrl+C to stop)…")
    try:
        while True:
            action = random.choice(ACTIONS)
            book_id = random.choice(BOOK_IDS)
            # refunds cheaper on average
            base = random.uniform(5, 40)
            price = base if action == "PURCHASE" else random.uniform(1, min(10, base))
            customer = random.choice(CUSTOMERS)
            log_line(action, book_id, price, customer)
            time.sleep(0.7)
    except KeyboardInterrupt:
        print("\nStopped.")
