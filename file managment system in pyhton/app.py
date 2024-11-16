import os

def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"File name {filename}:Created succesfully!")

    except FileExistsError:
        print(F'File name {filename} already exists!' )

    except Exception as E:
        print('An error occured') 



def view_all_file():
    files = os.listdir()
    if not files:
        print('No files found')

    else:
        print('Files in directory')
        for file in files:
            print(file)   


def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully!')

    except FileNotFoundError :
        print('file not found')       

    except Exception as e:
        print('An error occured!')        


def read_file(fiilename):
    try:
        with open ('sample.txt','r') as f:
            content = f.read()
            print(f"content of '{filename}' :\n{content}")


    except FileNotFoundError:
        print(f"{fiilename} dosen't exist")

    except Exception as e:
        print('An error occurred')




def  edit_file(fiilename):
    try:
        with open('sample.txt','a') as f:
            content = input('Enter data to add = ')
            f.write(content + "\n")
            print('content added to {filename} successuflly')

    except FileNotFoundError:
        print(f"{fiilename} dosen't exist")   




    except Exception as e:
        print('An error occurred')  




def main():
    while True:
        print('FILE MANAGMENT APP')
        print('1: Create file')
        print('2: View all files ')
        print('3: Delete all files')
        print('4: read file')
        print('5: edit file')
        print('6: Exit')
        



        choice=input('Enter your choice(1-6)=')

        if choice =='1':
            filename = input("Enter the file-name to create =")
            create_file(filename)


        elif choice =='2':
            view_all_file()

        elif choice =='3':
            filename=input('Enter a file you want delete')
            delete_file()
        
        elif choice =='4':
            filename =input('Enter file name to read')
            read_file(filename)


        elif choice =='5':
            filename = input('filename:Any)->None=')
            edit_file(filename)

        elif choice =='6':
            print('Closing th app.....')
            break


        else:
            print('In-valid syntax')


if __name__ == "__main__":
    main()
