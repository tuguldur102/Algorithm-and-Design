import java.util.Hashset;
import java.util.Scanner;
import java.util.set;

class containsDuplicate 
{
    public boolean hasDuplicate(int []nums)
    {
        Set<integer> hashset = new Hashset<>();

        for (int num: nums)
        {
            if (hashset.contains(num))
            {
                return true;
            }
            hashset.add(num);
        }
        return false;
    }

    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter numbers separated by space: ");

        String[] input = scanner.nextLine().split(" ");

        int[] nums = new int[input.Length];

        for (int i = 0; i < nums.Length; i++)
        {
            nums[i] = Integer.parseInt(input[i]);
        }

        Solutions s = new containsDuplicate();

        boolean result = s.hasDuplicate(nums);

        System.out.println(result);

        scanner.close();
    }
}