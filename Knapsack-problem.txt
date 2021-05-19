
package algo;
import java.util.Arrays;

/**
 *
 * @author Andrew Yasser
 */
// driver program with the approaches functions by creating object from each class and calling functions
public class Main {
public static void main (String [] args){
int number_of_items = 3;
Item[] list= new Item [number_of_items] ;
int capacity= 50;
 list[0] = new Item(15, 30);
 list[1] = new Item(30, 60);
 list[2]= new Item(45,90);
Arrays.sort(list, 1, list.length); 
int vals[] = new int[] { 30, 60, 90 }; 
int weights[] = new int[] { 15, 30, 45 };  
// dynamic programming solution
Dynamic_program_Knapsack K1 = new Dynamic_program_Knapsack();
int solution1 = K1.solution(capacity, vals, weights,  number_of_items);
System.out.println("solution using dynamic programming approach");
System.out.println(solution1);

// divide and conquer solution 
Recursive_Knapsack K2 = new Recursive_Knapsack();
int solution2 = K2.solution(capacity, vals , weights , number_of_items );
System.out.println("solution using divide and conquer approach");
System.out.println(solution1);
// Greedy solution
Greedy_knapsack K3 = new Greedy_knapsack();
System.out.println("solution using Greedy approach");
System.out.println(K3.solution(capacity, vals, weights,  number_of_items));
//Brute force solution
int K4 = Knapsack_Bruteforce.tryAllsolutions(number_of_items, weights, vals,  capacity );
System.out.println("solution using Brute force approach");
System.out.println(K4);
//Branch and bound solution 
BB_knapsack K5 = new BB_knapsack(list,capacity);
K5.knapsack();
System.out.println("solution using B&B approach");
K5.outputSolution();
//backtracking solution
double b = Backtracking_knapsack.backtracking(list, 0, 0, 0, capacity);
System.out.println("solution using Backtracking approach");
System.out.println(b);
}}










package algo;

/**
 *
 * Andrew Yasser 
 */

public class Knapsack_Bruteforce {
    public static int tryAllsolutions(int numberOfitems, int weights[], int vals[] ,int knapsack_capacity){
        // number of items 5
        int possiblities = (int) Math.pow(2, numberOfitems);
        int Max_Val = 0 ;
        for (int i = 0; i < possiblities; i++) {
            int temp_Val = 0; //<- current value
            int current_Weight = 0;
            String s = Integer.toBinaryString(i); // from integer to binary
            for (int j = 0; j < s.length(); j++) {
                if(s.charAt(j) == '1'){
                    temp_Val += vals[vals.length - j -1];  // current item vale is added to the possibility value
                    current_Weight += weights[weights.length - j -1 ];} // current item weight is added to current posiibility weigh  
            }
            if( temp_Val > Max_Val && current_Weight <= knapsack_capacity ) //if temp larger max && currentweight less than or equal maxWeight;
                Max_Val = temp_Val ; //max is set equal to temp; 
        }
        return Max_Val;} }

package algo;


public class Item implements Comparable<Item> {
double value ;
double weight;
boolean selected = false;

public Item( int weight, int value )
{
this.value = value;
this.weight = weight;

}

    @Override
    public int compareTo(Item o) {
        double ratio= this.value / this.weight ;
        double ratio2 = o.value / o.weight ;
        if (ratio > ratio2)
            return 1;
        else if (ratio < ratio2)
                return -1;
        else return 0;
    }
}



package algo;

import java.util.Arrays;

/**
 *
 * @author Andrew Yasser
 */


// Greedy approach 
public class Greedy_knapsack {
    
    double solution ( int Knapsack_weight, int value[] , int Weight[], int n)
{
// to store the current weight
double Current_weight =0 ;
// MAx value obtained
double Max_value = 0;
//bitstring to store solution
int sol [] = new int [n]; 
//initiallising the solution to be zeros as no items are selected yet
for (int i =0 ; i<n ; i++)
sol[i]=0;

// creating an array for value-to-weight ratios
double Ratios[] = new double[n]; 

//intilallising that arrays at first with zeros
for (int i =0 ; i<n ; i++)
Ratios[i]=0;

// calculating the value to weight ratios
for (int j=0 ; j <n ; j++)
Ratios[j] = value[j]/Weight[j];    

//sorting the ration in non-increasing order
Arrays.sort(Ratios, 0, n);

//determining whther to take the kth item or not
for (int k =0 ; k< n ; k ++)
{
Current_weight = Weight[k] + Current_weight;
if (Current_weight< Knapsack_weight )
    {
    sol[k]=1;
    }
} 
for (int s =0 ; s< n ; s ++)
{
if (sol[s] == 1 )
    {
    Max_value = Max_value + value[s];
    }
}
return Max_value;
}
}



package algo;

/**
 *
 * Andrew Yasser
 */


// Dynamic proograamming
public class Dynamic_program_Knapsack {
  static int solution(int Knapsack_weight, int value[], int weight[], int n) 
    { 
        //  uses memoization
        int  memo[][] = new int[n + 1][Knapsack_weight + 1]; 
        for (int i = 0; i <= n; i++) { 
            for (int w = 0; w <= Knapsack_weight; w++) { 
                if (i == 0 || w == 0) 
                    memo[i][w] = 0; 
                else if (weight[i - 1] <= w) 
                    memo[i][w] = Math.max( 
                        value[i - 1] + memo[i - 1][w - weight[i - 1]], 
                        memo[i - 1][w]); 
                else
                    memo[i][w] = memo[i - 1][w]; 
            } 
        } 
  
        return memo[n][Knapsack_weight]; 
    } 
}


package algo;

/**
 *
 * @author Andrew Yasser
 */
// Backtracking knapsack
public class Backtracking_knapsack {
     static double best_solution = 0;
     static double best_weight = 0;
        public static double backtracking(Item items[], double Max_value_obtained, double Current_sol_weight, int index,int capacity)
        {
            
            int[] y_bits = new int[items.length];
            int[] X_bits = new int[items.length]; 
            Backtracking_knapsack K6 = new Backtracking_knapsack(); 
            if ( index < items.length && Current_sol_weight + items[index].weight <= capacity)
            {
                y_bits[index] = 1;
                if (index < items.length)
                    backtracking( items , Max_value_obtained + items[index].value, Current_sol_weight + items[index].weight, index + 1, capacity);
                if (Max_value_obtained + items[index].value > best_solution && index == items.length -1)
                {   // copies y_bits to X_bits
                     K6.transfere_Sol(y_bits, X_bits);
                    best_solution = Max_value_obtained + items[index].value;
                    best_weight = Current_sol_weight + items[index].weight;
                }
            }
            if (index < items.length && bound( items, Max_value_obtained, Current_sol_weight, index, capacity ) >= best_solution)
            {
                y_bits[index] = 0;
                if (index < items.length)
                    backtracking(items, Max_value_obtained , Current_sol_weight , index + 1, capacity);
                if (Max_value_obtained > best_solution && index == items.length -1)
                {
                    K6.transfere_Sol(y_bits, X_bits) ;
                    //y_bits.CopyTo(X_bits, 0);
                    best_solution = Max_value_obtained;
                    best_weight = Current_sol_weight;
                }
            }
            return best_solution;
        }
        // function to copy an array to another
        void transfere_Sol( int A[], int B []) 
        {     
        for(int i=0; i<A.length; i++) {
                   B[i]=A[i];
                                }
         
        }
        // bounding function
        static double bound ( Item items[], double Max_value_obtained, double Current_sol_weight, int index, int capacity)
        { 
         double b = Max_value_obtained;
         double c = Current_sol_weight;
            for (int i = index; i < items.length ; i++) {
                c += c + items[i].weight ;
                if (c< capacity) 
                    b = b+items[i].value;
                else return b +(1-(c-capacity)/ items[i].weight* items[i].value);
                }
                return b ; 
                }
            }



















package algo;

/**
 *
 * @author DELL
 */
//Branch and bound
public class BB_knapsack {
    
    
    private Item[] items; // Input list of items
private int capacity ; //Maxweight allowed in knapsack
private int[] x; // Best solution array: item i in if xi=1
private int[] y; // Working solution array at current tree node
private double solutionProfit= -1; // Profit of best solution so far
private double currWgt; // Weight of solution at this tree node
private double current_val; // Profit of solution at this tree node
private double nw_weight; // Weight of solution from bound() method
private double Max_Value; // max value of solution from bound() method
private int k; 
private int curr_Item	 ; 
public BB_knapsack (Item[] i, int c) {
items= i;
capacity= c;
x= new int[items.length];
y= new int[items.length];
} 

public void knapsack() {
int n= items.length; // No. of items in problem
do { // While upper bound < known solution so far,backtrack
while (bound() <= solutionProfit) {
while (k != 0 && y[k] != 1) // Back up if item k is not included
k--; 
if ( k == 0) //If the root reached then return.
return;
y[k]= 0; // Else don't include k (Right branch)
currWgt -= items[k].weight; 
current_val -= items[k].value; 
} 
currWgt= nw_weight; 
current_val= Max_Value; 
k= curr_Item; 

if (k == n) { 
solutionProfit= current_val; 
System.arraycopy(y, 0, x, 0, y.length); // Copy soln into array x
k= n-1; 
} else 
y[k]= 0; 
} while (true); 
}
private double bound() {
boolean found= false; 
double boundVal= -1; // upper bound value
int n= items.length; // No. of items in problem
Max_Value= current_val; 
nw_weight= currWgt;
curr_Item= k+1; 
while (curr_Item < n && !found) { // More items & haven’t found partial values
if (nw_weight + items[curr_Item].weight <= capacity) { // If fits
nw_weight += items[curr_Item].weight; // Update the new weight
Max_Value += items[curr_Item].value; 
y[curr_Item]= 1; // Update current solution to show item k is in it
} else {  
boundVal = Max_Value + (capacity - nw_weight)*items[curr_Item].value/items[curr_Item].weight;   
found = true; } // calculate upper bound
curr_Item++; // Go to next item and try to put in sack
}
if (found) { // If we have fractional soln for last item in sack, get back to prvious item
curr_Item--; 
return boundVal; // Return the upper bound
} else {
return Max_Value;// Return max value including last item
} } 

public void outputSolution () { 
int totalProfit= 0; 
int totalWeight= 0; 
System.out.println("Items taken:");
    for (int i = 0; i < x.length; i++) {
        if (x[i] != 0){
         System.out.println(items[i]);
         totalProfit += items[i].value;
         totalWeight += items[i].weight;}
        System.out.println("\nProfit: " + totalProfit);
        System.out.println("\nweight: " + totalWeight);
         
        }
    }

}

import static sun.rmi.transport.TransportConstants.Return;

/* Andrew Yasser*/

// Divide and conquer
public class Recursive_Knapsack {
static int solution ( int Knapsack_weight, int value[] , int Weight[], int n)
{
if (n==0 || Knapsack_weight == 0) //base condition
return 0 ;

 if (Weight [n - 1] > Knapsack_weight) 
return solution (Knapsack_weight,  value, Weight,  n - 1); // checking whther the nth item can be selected in the solution by being                                                          //fit in the knapsack or not
 else
 
            return Math.max(
                value [n - 1] + solution (Knapsack_weight - Weight [n - 1], 
                                      Weight, value, n - 1), 
                solution (Knapsack_weight, value,Weight , n - 1));
} // the max of value whther the nth item is included or not
}
