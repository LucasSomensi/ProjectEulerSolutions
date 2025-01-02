import java.util.ArrayList;

public class Problem201{
	
	public static final boolean useExampleSet = false;
	public static final int initialSetSize = 100;
	public static final int subsetSize = 50;
	public static ArrayList<Integer> initialSet;
	public static int biggestPossibleSum;
	public static int setSize;
	
	
	public static void firstStep(boolean[][] mainMatrix){
		for (int i = 0; i<setSize; i++){
			mainMatrix[initialSet.get(i)][i] = true;
		}
	}
	
	public static void nextStep(boolean[][] mainMatrix, boolean[][] markedMatrix){
		boolean[][] nextMainMatrix = new boolean[mainMatrix.length][mainMatrix[0].length];
		boolean[][] nextMarkedMatrix = new boolean[markedMatrix.length][markedMatrix[0].length];
		
		for (int l = 0; l<mainMatrix.length; l++){
			for (int c = 0; c<mainMatrix[0].length; c++){
				if (mainMatrix[l][c]) {
					for (int newColumn = c+1; newColumn<mainMatrix[0].length; newColumn++){
						int newLine = l+initialSet.get(newColumn);
						if (!nextMainMatrix[newLine][newColumn]){
							nextMainMatrix[newLine][newColumn]=true;
							nextMarkedMatrix[newLine][newColumn]=markedMatrix[l][c];
						} else {
							nextMarkedMatrix[newLine][newColumn]=true;
						}
					}
				}
			}
			
		}
		
		for (int l = 0; l<mainMatrix.length; l++){
			for (int c = 0; c<mainMatrix[0].length; c++){
				mainMatrix[l][c] = nextMainMatrix[l][c];
				markedMatrix[l][c] = nextMarkedMatrix[l][c];
			}
		}
		
	}
	
	public static void lastTrim(boolean[][] mainMatrix){
		boolean remove = false;
		for (int l = 0; l<mainMatrix.length; l++){
			remove = false;
			for (int c = 0; c<mainMatrix[0].length; c++){
				if (mainMatrix[l][c] && (!remove)) remove = true;
				else if (mainMatrix[l][c] && remove) {
					for (int cline = 0; cline<mainMatrix[0].length; cline++){
						mainMatrix[l][cline]=false;
					}
					break;
				}
			}
		}
	}
	
	public static int sumAll(boolean[][] mainMatrix, boolean[][] markedMatrix){
		int result = 0;
		for (int l = 0; l<mainMatrix.length; l++){
			for (int c = 0; c<mainMatrix[0].length; c++){
				if (mainMatrix[l][c] && (!markedMatrix[l][c])){
					result+=l;
				}
			}
		}
		return result;
	}
	
	public static void main(String[] args){
		

		initialSet = new ArrayList<Integer>();
		biggestPossibleSum = 0;
		int totalIterations;
		if (useExampleSet){
			initialSet.add(1); initialSet.add(3); initialSet.add(6);
			initialSet.add(8); initialSet.add(10); initialSet.add(11);
			biggestPossibleSum = 11+10+8;
			totalIterations = 3;
		} else {
			for (int n = 1; n<=initialSetSize; n++){
				initialSet.add(n*n);
				if ((initialSetSize-n)<subsetSize) biggestPossibleSum+=(n*n);
			}
			totalIterations = subsetSize;
		}
		setSize = initialSet.size();
		initialSet.trimToSize();
		
		//initializing the first step matrix
		boolean[][] mainMatrix = new boolean[biggestPossibleSum+1][setSize];
		boolean[][] markedMatrix = new boolean[biggestPossibleSum+1][setSize];
		
		firstStep(mainMatrix);
		
		for (int i = 1; i<totalIterations; i++){
			nextStep(mainMatrix, markedMatrix);
		}
		

		System.out.println();
		lastTrim(mainMatrix);
		System.out.println(sumAll(mainMatrix, markedMatrix));
		
		
	}
	
}