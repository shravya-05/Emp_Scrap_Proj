import os

print("\nRunning Scraper...")
os.system("python scraper.py")

print("\nRunning Normalization...")
os.system("python normalize_data.py")

print("\nRunning Tests...")
os.system("python -m unittest test_scraper.py")
os.system("python -m unittest test_normalization.py")

print("\nCompleted!")
