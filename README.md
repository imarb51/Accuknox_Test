### Answer to the Django Signal Questions:

1. **By default, are Django signals executed synchronously or asynchronously?**
   - **Answer**: By default, Django signals are executed **synchronously**. This means that when a signal is triggered, it is handled immediately, blocking the execution of the remaining code until the signal handler has finished. There is no asynchronous execution unless you explicitly make it asynchronous, such as by using background tasks (e.g., Celery) or threading.

2. **Do Django signals run in the same thread as the caller?**
   - **Answer**: Yes, Django signals run in the **same thread** as the caller by default. Since Django signals are synchronous by nature, they execute within the same thread context as the function that triggered the signal. This can be seen by printing the current thread name in both the calling function and the signal handler, which would show the same thread for both.

3. **By default, do Django signals run in the same database transaction as the caller?**
   - **Answer**: Yes, Django signals run in the **same database transaction** as the caller by default. This means if a signal is emitted inside an atomic transaction block, the signal handler will execute as part of that transaction. If the transaction is rolled back, the signal’s effects (if they involve database operations) are also rolled back.

### Explanation of the Custom Rectangle Class:

- The `Rectangle` class has two attributes, `length` and `width`.
- By defining the `__iter__` method, we make the class iterable, allowing it to return its length and width in sequence as dictionaries when looped over.