# SVM 모델로 이미지 분류
# 세계 정치인들 중 일부 얼굴 사진 데이터를 사용
from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
import koreanize_matplotlib

faces = fetch_lfw_people(min_faces_per_person=60, color=False, resize=0.5)
# 60 : 한 사람 당 60장 이상의 사진이 있는 자료만 사용
# print(faces)
print(faces.data)
print(faces.data.shape)
print(faces.target)
print(faces.target_names)
print(faces.images.shape)
print()
print(faces.images[1])
print(faces.target_names[faces.target[1]])
plt.imshow(faces.images[1],cmap='bone')
plt.show()

# fig, ax = plt.subplots(3,5)
# for i, axi in enumerate(ax.flat):
#     axi.imshow(faces.images[i],cmap='bone')
#     axi.set(xticks=[],yticks=[],xlabel=faces.target_names[faces.target[i]])
# plt.show()

n = 150
m_pca = PCA(n_components=n, whiten=True, random_state=0)
x_low = m_pca.fit_transform(faces.data)

fig, ax = plt.subplots(3,5, figsize=(10,6))
for i, axi in enumerate(ax.flat):
    axi.imshow(m_pca.components_[i].reshape(faces.images[0].shape),cmap='bone')
    axi.axis('off')
    axi.set_title(f'PC {i+1}')
plt.show()
# SVM 알고리즘은 실제 얼굴이 아니라 특징 패턴으로 분류작업을 한다. 

# 설명력
print(m_pca.explained_variance_ratio_[:10])
print(m_pca.explained_variance_ratio_.sum())
# n =100개로 얼마나 원본 정보를 유지했는지 확인함

# 원본 vs 복원 이미지 비교
x_reconst = m_pca.inverse_transform(x_low)
fig, ax = plt.subplots(2,5,figsize=(10,4))
for i in range(5):
    ax[0,i].imshow(faces.images[i], cmap='bone')
    ax[0,i].set_title('원본')
    ax[0,i].axis('off')
    
    ax[1,i].imshow(
        x_reconst[i].reshape(faces.images[0].shape),cmap='bone'
    )
    ax[1,i].set_title('복원')
    ax[1,i].axis('off')
plt.suptitle('PCA 복원 비교', fontsize=12)
plt.tight_layout()
plt.show()

svcmodel = SVC(C=1,random_state=111)
mymodel = make_pipeline(m_pca, svcmodel)
print(mymodel)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(faces.data, faces.target, random_state=1, stratify=faces.target)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
print(x_train[0])
print(y_train[0])

mymodel.fit(x_train, y_train)
pred = mymodel.predict(x_test)
print('예측값 ', pred[:10])
print('실제값 ', y_test[:10])

# 정확도 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
confmat = confusion_matrix(y_test, pred)
print('confusion \n', confmat)
print(accuracy_score(y_test, pred))
print(classification_report(y_test, pred, target_names=faces.target_names))

# 기존 데이터로 테스트
test_img = faces.data[0].reshape(1,-1)
print(test_img)
test_pred = mymodel.predict(test_img)
print(faces.target_names[test_pred[0]])
print(faces.target_names[faces.target[0]])

print()
# 새로운 데이터 사용
from PIL import Image
import numpy as np
img = Image.open('bush.jpeg')
img = img.convert('L')
img = img.resize((47,62))
# numpy 이미지는 h,w
# PIL 이미지는 w,h
img_np = np.array(img)
# print(img_np)
img_np = img_np / 255 # 정규화 (학습 데이터와 맞추기)
img_flat = img_np.reshape(1,-1)

new_pred = mymodel.predict(img_flat)
print(faces.target_names[new_pred[0]])
plt.imshow(img_np, cmap='bone')
plt.show()
