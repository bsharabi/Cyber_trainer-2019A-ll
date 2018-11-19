import passlib.hash

All_hash="root:$6$Tnd5Ce9O$nNhq84wKYQQwxKGqsBAsIMHIETB9MjOeO9ykuOmW9q6PO1v4qWEuCbfQKYQXK4D2uJjvgrkfnZfcMWqlQhOOm/:1784table_sum6:0:99999:7:::"
hash2="$6$Tnd5Ce9O$nNhq84wKYQQwxKGqsBAsIMHIETB9MjOeO9ykuOmW9q6PO1v4qWEuCbfQKYQXK4D2uJjvgrkfnZfcMWqlQhOOm/"
salt = "Tnd5Ce9O"
str1 = "abcdefghijklmnopqrstuvwxyz0123456789"

def hash():
    print(hash2)
    for i in str1 :
        for j in str1 :
            for k in str1 :
                for l in str1 :
                    for m in str1 :
                        for o in str1 :
                            pass1 = i+j+k+l+m+o
                            encode = passlib.hash.sha512_crypt.encrypt(pass1, salt=salt, rounds=5000)
                            print(encode)
                            if(encode==hash2):
                                print("The code is : "+pass1)
                                return 0
                            
'''
-----------OUT PUT-----------
"The code is : 1a2s3d"
 '''