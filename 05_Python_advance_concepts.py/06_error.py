# while(True) :
#     try :
#         a = int(input("Enter value: "))
#         print(a)
#     except ValueError:
#         print("Hey plz dont perform bad typecast")

#     except Exception as e:
#         print("Some Error has Occured!!",e)


# try :
#     a = 324/10
# except Exception as e:
#     print(e)

# else :
#     print("No error occured")


try :
    a = 324/10
    print(a)
except Exception as e:
    print(e)

finally:
    print("Exceuted always")