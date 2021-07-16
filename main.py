import os
from os import listdir
from os.path import isfile, join
import cv2
from matplotlib import pyplot as plt
from scipy import ndimage


def plot(image1, image2):
    fig = plt.figure(figsize=(9, 6))
    plt.subplots_adjust(wspace=0.25, hspace=0.25)
    plt.axis('off')
    fig.suptitle(numb2 + 'Matches')

    sub1 = fig.add_subplot(2, 2, (3, 4))  # two rows, two columns, fist cell
    plt.annotate('ORB Aplicado', xy=(0.5, -0.5), va='center', ha='center', weight='bold', fontsize=10)
    plt.axis('off')
    sub1.imshow(image1)

    # Create third axes, a combination of third and fourth cell
    sub3 = fig.add_subplot(2, 2, (1, 2))  # two rows, two colums, combined third and fourth cell
    plt.annotate('Imagem Inicial', xy=(0.5, -0.5), va='center', ha='center', weight='bold', fontsize=10)
    plt.axis('off')
    sub3.imshow(image2)


def points(image1, image2):
    query_img = cv2.imread(image1)
    train_img = cv2.imread(image2)

    query_img_bw = cv2.cvtColor(query_img, cv2.COLOR_BGR2GRAY)
    train_img_bw = cv2.cvtColor(train_img, cv2.COLOR_BGR2GRAY)

    # Initialize the ORB detector algorithm
    sift = cv2.ORB_create(nfeatures=500)

    # Now detect the keypoints and compute
    # the descriptors for the query image
    # and train image
    queryKeypoints, queryDescriptors = sift.detectAndCompute(query_img_bw, None)
    trainKeypoints, trainDescriptors = sift.detectAndCompute(train_img_bw, None)

    # Initialize the Matcher for matching
    # the keypoints and then match the
    # keypoints
    matcher = cv2.BFMatcher()
    matches = matcher.match(queryDescriptors, trainDescriptors)

    # draw the matches to the final image
    # containing both the images the drawMatches()
    # function takes both images and keypoints
    # and outputs the matched query image with
    # its train image
    final_img = cv2.drawMatches(query_img, queryKeypoints,
                                train_img, trainKeypoints, matches[:20], None)

    features = sift.detect(query_img, None)
    final_img_des = cv2.drawKeypoints(query_img, features, None, color=(0, 255, 0), flags=0)

    final_img = cv2.resize(final_img, (1000, 500))

    lista1 = [queryKeypoints[matches.queryIdx].pt for matches in matches]
    lista2 = [trainKeypoints[matches.trainIdx].pt for matches in matches]

    # lista1, lista2 = getpoints(matches, queryKeypoints, trainKeypoints)
    # Show the final image
    # cv2.imshow("Matches", final_img)

    # Imagem tratada
    #angles = [queryKeypoints[i].angle for i in range(len(queryKeypoints))]
    #rotated_img = ndimage.rotate(train_img, sum(angles) / len(angles), reshape=False)

    plot(final_img, train_img)

    os.chdir('C:/Users/asus/PycharmProjects/ORB1/' + 'Resultados-' + where)
    plt.savefig(numb2 + 'Matches.jpg')
    f = open(numb2 + 'Points.txt', "w")
    f.write('Pontos :\n' + str(lista2))
    f.close()
    plt.close()


where1 = ['DataBase/saved']  # [AfterDTC Frames]
prefix = ''  # 'l'     #[H frame]
where=where1[0]
mypath = 'C:/Users/asus/PycharmProjects/ORB1/' + where
list1 = [f for f in listdir(mypath) if isfile(join(mypath, f))]


image1 = 'C:/Users/asus/PycharmProjects/ORB1/DataBase/compared.png'
for j in list1:
    print(str(j) + ' adding....')
    image2 = 'C:/Users/asus/PycharmProjects/ORB1/' + where + '/' + prefix + str(j)
    numb2 = j  # ''.join(filter(str.isdigit, str(image2)))
    points(image1, image2)
    print(str(j) + ' added!')