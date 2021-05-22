import instaloader

test = instaloader.Instaloader()
acc = input('Enter the Account Username: ')

#acc = 'leomessi'
test.download_profile(acc, profile_pic_only = True)

