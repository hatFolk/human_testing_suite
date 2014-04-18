
def subroutine () :
    print ("\n\t--> I am subroutine.")
    print ("\n\t--> I accepted no arguments.")
    print ("\n\t--> I'm printing stuff, doing work.")
    print ("\n\t--> Now that I'm done, I just cede control back to the call site.\n")


def main():
    print ("\n* main function is starting...")
    print ("* main function is calling subroutine:")
    subroutine()
    print ("\n* main resumed after we finished the call to subroutine.\n")

main()

# Notice that the subroutine() call is not assigned to anything.
# Because the function doesn't explicitly return a value, this is fine.
# It returns a None, which gets ignored by main.
