  class QuickSort:
      def sort(self, arr):
          self.quick_sort(arr, 0, len(arr) - 1)
          return arr

      def quick_sort(self, arr, low, high):
          if low < high:
              pi = self.partition(arr, low, high)
              self.quick_sort(arr, low, pi - 1)  # 對分割後的兩個子數組進行遞歸排序
              self.quick_sort(arr, pi + 1, high)

      def partition(self, arr, low, high):
          pivot = arr[high]
          i = low - 1
          for j in range(low, high):
              if arr[j] < pivot:
                  i += 1
                  arr[i], arr[j] = arr[j], arr[i]  # 交換元素
          arr[i + 1], arr[high] = arr[high], arr[i + 1]
          return i + 1


  if __name__ == "__main__":
      qs = QuickSort()
      array = [3, 6, 8, 10, 1, 2, 1]
      sorted_array = qs.sort(array)
      print(sorted_array)
