"""stats() takes any amount of numbers and returns three answers. Unpack them 
like Day 05. If nothing is sent, return None.."""
# Your job:
# 1. make a list marks = [67, 45, 92, 78]
#    and call stats(*marks)
# 2. also return how many numbers were sent
def stats(*numbers):
    if len(numbers) == 0:
        return None
    average = round(sum(numbers) / len(numbers), 2)
    return min(numbers), max(numbers), average, len(numbers)

low, high, avg, count = stats(12, 45, 7, 30)
print(f"List1:\nLow: {low}, High: {high}, Average: {avg}, Count:{count}")
# Low: 7, High: 45, Average: 23.5

marks = [67, 45, 92, 78]
m_low, m_high, m_avg, m_count = stats(*marks)
print(f"List2(marks):\nLow: {m_low}, High: {m_high}, Average: {m_avg}, Items Sent: {m_count}")
