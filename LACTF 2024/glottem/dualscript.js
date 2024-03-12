/* Python code will ignore this line */
// <Ignore by Python> 
const args = process.argv;
const flag = "secretFlag"; // Set your flag value here

// Check if the flag is provided and matches
if(args.length > 2 && args[2] === flag) {
  console.log('correct');
} else {
  console.log('incorrect');
}

/*
Valid Python code starts here. JavaScript will ignore the rest of the file
due to the block comment.
*/
// <Ignore by JavaScript>
if __name__ == "__main__":
    import sys
    flag = "secretFlag"  # Set your flag value here
    
    # Check if the flag is provided and matches
    if len(sys.argv) > 1 and sys.argv[1] == flag:
        print('correct')
    else:
        print('incorrect')
# End of Python code
