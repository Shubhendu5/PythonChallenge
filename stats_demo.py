def summarize(numbers):

    """Return a dict with count, mi."""

    if not numbers:

        raise ValueError("Empty list provided")

    total = sum(numbers)

    return {

        "count": len(numbers),

        "min": min(numbers),

        "max": max(numbers),

        "sum": total,

        "avg": total / len(numbers)

    }



def main():

    sample = [3, 7, 2, 9, 4, 10, 5]

    stats = summarize(sample)

    print("Input numbers:", sample)

    print("Count:", stats["count"])

    print("Min:", stats["min"])

    print("Max:", stats["max"])

    print("Sum:", stats["sum"])

    print("Average:", round(stats["avg"], 2))



if __name__ == "__main__"


//Shubhendu Banerjeeshubhendushubhendu
shubhendu
