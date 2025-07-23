int getSecondLargest(int *arr, int n) {
    int first = -1, second = -1;

    for (int i = 0; i < n; i++) {
        if (arr[i] > first) {
            second = first;
            first = arr[i];
        } else if (arr[i] < first && arr[i] > second) {
            second = arr[i];
        }
    }

    return second;
}
