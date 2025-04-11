# Title

![image](https://github.com/user-attachments/assets/4995e32a-deed-4241-8bd6-5d2b42bb36ff)

---
---

# ABSTRACT 초록

**Accurate segmentation and analysis for each animal in surveillance video images will help poultry farmers to monitor and promote animal welfare.**  
감시 영상 속 각 동물의 정확한 분할 및 분석은 양계 농가가 동물을 모니터링하고 복지를 증진하는 데 도움이 됩니다.

**However, it is challenging to accurately segment each animal due to the similar appearance, different scales, rapid growth and adhesive areas of group animals.**  
하지만 무리지어 있는 동물들의 유사한 외형, 다양한 크기, 빠른 성장, 그리고 서로 붙어 있는 영역 때문에 개별 동물을 정확하게 분할하는 것은 어렵습니다.

**Meanwhile, lacking of useful training data also limits the effectiveness of animal segmentation algorithms.**  
한편, 유용한 학습 데이터의 부족도 동물 분할 알고리즘의 성능을 제한합니다.

**To address these problems, we first construct a chicken image segmentation dataset to study the behavior of chickens for intelligent monitoring and analysis.**  
이러한 문제를 해결하기 위해, 우리는 먼저 지능형 모니터링 및 분석을 위한 닭의 행동을 연구할 수 있는 닭 이미지 분할 데이터셋을 구축했습니다.

**Then, we propose an effective end-to-end framework for chicken image segmentation, which can also be used for other animal image segmentation.**  
그 다음, 닭 이미지 분할을 위한 효과적인 엔드-투-엔드 프레임워크를 제안하며, 이는 다른 동물의 이미지 분할에도 사용될 수 있습니다.

**An end-to-end multi-scale based encoder-decoder network is first utilized to extract multi-scale features.**  
우선, 다중 스케일 기반의 엔드-투-엔드 인코더-디코더 네트워크를 이용해 다양한 스케일의 특징을 추출합니다.

**Then, an attention-based module is employed to extract and intensify effective features, thus better segmentation results can be obtained.**  
그 다음, 주의(attention) 기반 모듈을 사용해 유효한 특징을 추출하고 강조함으로써, 더 나은 분할 결과를 얻을 수 있습니다.

**Finally, a multi-output combined loss function is proposed to make effective supervision for better segmentation.**  
마지막으로, 더 나은 분할을 위한 효과적인 학습 지도를 위해 다중 출력 결합 손실 함수가 제안됩니다.

**Experimental results demonstrate the promising performance of the proposed framework for chicken image segmentation.**  
실험 결과는 제안된 프레임워크가 닭 이미지 분할에서 유망한 성능을 보임을 보여줍니다.

![image](https://github.com/user-attachments/assets/65d90ce9-225a-43be-9589-91d2a7a89265)

---
---

# I. INTRODUCTION 서론

**Recently, many studies focus on observing and analyzing the behaviour of animal to prevent diseases for animal welfare [1].**  
최근 동물 복지를 위한 질병 예방을 목적으로 동물의 행동을 관찰하고 분석하는 연구가 활발히 진행되고 있습니다 [1].

**The rapid development of artificial intelligence and image processing technology accelerates the process of automatic and intelligent farming.**  
인공지능과 영상처리 기술의 빠른 발전은 자동화되고 지능적인 농업의 발전을 가속화하고 있습니다.

**Observing and analyzing animal automatically can be achieved by sensor-based methods [2], [3] and computer vision based methods [4]–[6].**  
동물을 자동으로 관찰하고 분석하는 방법은 센서 기반 방식 [2], [3]과 컴퓨터 비전 기반 방식 [4]–[6]으로 나눌 수 있습니다.

**For the former, specific sensor devices are used to obtain information of position, number, etc.**  
전자의 경우, 특정 센서 장비를 통해 위치, 수량 등의 정보를 수집합니다.

**For examples, classical ear tags or collars can be exploited to locate positions of animals, however, it is very expensive and time-consuming to wear sensors for each animal.**  
예를 들어, 전통적인 귀표나 목걸이 센서를 이용해 동물의 위치를 파악할 수 있으나, 모든 개체에 장착하는 것은 매우 비용이 많이 들고 시간이 오래 걸립니다.

**For the latter, video or image data of animals need to be captured by cameras firstly, and then these data are processed by computer vision based methods for intelligent farming.**  
후자의 경우, 카메라로 동물의 영상이나 이미지를 촬영한 후 컴퓨터 비전 기반 방법으로 처리하여 지능형 농업에 활용합니다.

**The advantages of low price, easy installation and non-invasion make computer vision based methods more preferentially to monitor animal behavior [3].**  
컴퓨터 비전 기반 방식은 저렴한 가격, 쉬운 설치, 비침습성 등의 장점으로 인해 동물 행동 모니터링에 더 선호됩니다 [3].

**Hence, in this paper, we mainly focus on computer vision based techniques for intelligent farming.**  
따라서 본 논문에서는 컴퓨터 비전 기반의 지능형 농업 기술에 중점을 둡니다.

---

**Image segmentation, as the basic and important step to monitor animal health, has drawn lots of attentions in intelligent farming [3], [4], [7].**  
이미지 분할은 동물 건강을 모니터링하기 위한 기본적이면서 중요한 과정으로, 지능형 농업에서 많은 관심을 받고 있습니다 [3], [4], [7].

**Significant progress has been made to achieve more accurate segmentation results with the supervised framework of machine learning.**  
머신러닝의 지도학습 프레임워크를 활용하여 보다 정확한 분할 성능을 달성하는 데 있어 큰 진전이 있었습니다.

**Particularly, deep convolutional neural networks (CNN) based methods [5], [6], [8] have achieved the state-of-the-art performance for image segmentation.**  
특히, 딥 합성곱 신경망(CNN) 기반 방법 [5], [6], [8]은 이미지 분할 분야에서 최신의 성능을 보여주고 있습니다.

**Accurate segmentation and analysis will help people to monitor and reveal deviations of animal, and to prevent losses in animal production process.**  
정확한 분할과 분석은 동물의 이상 행동을 모니터링하고 조기에 발견하여 생산 과정의 손실을 예방하는 데 도움이 됩니다.

---

**In this paper, we focus on studying image segmentation of chicken due to its large market demand.**  
본 논문에서는 시장 수요가 큰 닭의 이미지 분할에 중점을 두고 연구합니다.

**Besides, the proposed segmentation framework can also be applied to other animals or objects segmentation.**  
또한 제안된 분할 프레임워크는 다른 동물이나 객체의 분할에도 적용할 수 있습니다.

**Individual chicken segmentation is the basic step to segregate from group-level treatment and conduct individual chicken care.**  
개별 닭 분할은 군집 단위 처리에서 벗어나 개별 닭 관리로 나아가기 위한 기본 단계입니다.

**Based on the segmented individual chicken, important information such as chicken position and chicken number can be obtained.**  
분할된 개별 닭을 바탕으로 닭의 위치와 수량 등 중요한 정보를 추출할 수 있습니다.

**Thus, we can monitor chicken behaviour constantly and regard these as indicators of health and well-being.**  
이를 통해 닭의 행동을 지속적으로 모니터링하고 건강과 복지의 지표로 활용할 수 있습니다.

---

**As observed, most chickens usually crowd together in a cage as shown in Fig. 1, it is challenging to monitor the behavior of group chickens by separating adhesive regions.**  
관찰된 바와 같이 대부분의 닭들은 Fig. 1에서처럼 우리 안에 밀집되어 있기 때문에, 서로 밀착된 영역을 분리해 무리 행동을 모니터링하는 것은 매우 어렵습니다.  
<p align="center">
    <img src="https://github.com/user-attachments/assets/42529c23-047d-4f0e-b516-c5889dd43ca1" alt="image" width="500">
</p>

**Besides, similar appearance and various scale, motion blur by chicken movement and object occlusions as shown in Fig. 2, which make it challenging for accurate chicken segmentation.**  
또한 Fig. 2에서 보이는 것처럼, 닭들의 유사한 외형, 다양한 크기, 움직임으로 인한 블러, 객체 가림 현상 등이 정확한 분할을 어렵게 만듭니다.  
<p align="center">
    <img src="https://github.com/user-attachments/assets/eb6058ad-f107-43c1-bbc6-5b7f5f2add28" alt="image" width="500">
</p>

> - Occlusion : 컴퓨터 비전 분야에서 어떤 물체 앞에 장애물이 있어서 가려지는 현상  
> - Adhesion : 부착

---

**To address these issues mentioned above, we propose a multi-scale attention based deep network, which is named MSAnet, for effective chicken image segmentation.**  
이러한 문제를 해결하기 위해, 우리는 효과적인 닭 이미지 분할을 위한 다중 스케일 주의 기반 딥 네트워크인 **MSAnet**을 제안합니다.

---

**The major contributions of this work include the followings.**  
**본 연구의 주요 기여는 다음과 같습니다.**

- **We construct a novel chicken dataset, which is captured by a monocular camera covered with different periods for chicken segmentation and behavior analysis.**  
  닭 이미지 분할 및 행동 분석을 위해, 다양한 기간에 걸쳐 단안 카메라로 촬영한 새로운 닭 데이터셋을 구축했습니다.

- **To the best of our knowledge, we are the first one to construct the chicken dataset for the research of chicken image segmentation and analysis.**  
  우리가 아는 한, 닭 이미지 분할 및 분석을 위한 닭 데이터셋을 구축한 것은 본 연구가 최초입니다.

- **We propose an automatic and effective end-to-end segmentation framework by a multi-scale deep network, which is robust to various scales by constructing an image pyramid to extract multi-scale features automatically.**  
  이미지 피라미드를 구성하여 다양한 스케일에 강건한 다중 스케일 딥 네트워크를 통해 자동적이고 효과적인 엔드-투-엔드 분할 프레임워크를 제안합니다.

- **To obtain more accurate segmentation performance, we propose an attention-based strategy which includes channel attention and edge attention for effective feature extraction.**  
  보다 정확한 분할 성능을 위해, 채널 주의와 에지 주의를 포함하는 주의 기반 전략을 제안하여 효과적인 특징 추출을 수행합니다.

- **A combined loss strategy based on multi-scale side-outputs is utilized to conduct effective deep supervision for the multi-scale network.**  
  다중 스케일 사이드 출력을 기반으로 한 결합 손실 전략을 통해 네트워크에 효과적인 학습 지도를 제공합니다.

- **We study different CNN-based segmentation methods for chicken segmentation on the constructed chicken database.**  
  구축된 닭 데이터베이스에서 다양한 CNN 기반 분할 방법을 실험적으로 비교합니다.

- **Experimental results demonstrate that the proposed approach achieves promising segmentation performance for chicken segmentation.**  
  실험 결과, 제안된 방법이 닭 이미지 분할에서 유망한 성능을 보임을 확인할 수 있습니다.

---

**The rest of this paper is organized as follows.**  
논문의 나머지 구성은 다음과 같습니다.

**Related previous work is reviewed in Sec. II.**  
II장에서 관련 선행 연구를 검토하고,

**The detailed methodology is described in Sec. III.**  
III장에서 방법론을 상세히 설명하며,

**Experimental results are presented in Sec. IV.**  
IV장에서 실험 결과를 제시하고,

**Finally, concluding remarks and future extensions are given in Sec. V.**  
마지막으로 V장에서 결론과 향후 연구 방향을 논의합니다.

---

![image](https://github.com/user-attachments/assets/e6525448-af37-42db-a150-1df97906e85e)


---
---

# II. RELATED WORK  관련 연구

**The behavioural research of animal can be greatly simplified by automatic and intelligent monitoring systems.**  
동물의 행동 연구는 자동화되고 지능적인 모니터링 시스템을 통해 크게 간소화될 수 있습니다.

**Recently, methods based on computer vision [5], [9] have shown the advantages to conduct effective evaluation without influence to the normal behaviour of the animals.**  
최근 컴퓨터 비전 기반 방법 [5], [9]은 동물의 정상 행동에 영향을 주지 않으면서 효과적인 평가를 수행할 수 있는 장점을 보여주고 있습니다.

**Animal segmentation is the basic and important step to monitor and analyze each animal separately.**  
동물 분할은 개별 동물을 모니터링하고 분석하기 위한 기초적이고 중요한 단계입니다.

---

**A. ANIMAL DETECTION AND ANALYSE**  
**A. 동물 탐지 및 분석**

**Many object detection and segmentation methods have been proposed to detect the individual animal [3], [4], [7], [10]–[12].**  
개별 동물을 탐지하기 위한 다양한 객체 탐지 및 분할 방법이 제안되었습니다 [3], [4], [7], [10]–[12].

**Kashiha et al. [10] proposed to label image and distinguish pigs by Otsu segmentation method.**  
Kashiha 등 [10]은 Otsu 분할 방법을 이용하여 이미지에 라벨을 붙이고 돼지를 구별하는 방법을 제안했습니다.

**Guo et al. [11] proposed a pig segmentation method by combining the mixed Gaussian model with the maximum entropy.**  
Guo 등 [11]은 혼합 가우시안 모델과 최대 엔트로피를 결합한 돼지 분할 방법을 제안했습니다.

**Guo et al. [12] proposed a multi-level threshold segmentation approach to obtain pig’s profile.**  
Guo 등 [12]은 다단계 임계값 분할 기법을 통해 돼지의 윤곽을 추출하는 방법을 제안했습니다.

**Vroegindeweij et al. [7] proposed a method for pixel segmentation based on spectral reflectance properties.**  
Vroegindeweij 등 [7]은 스펙트럼 반사 특성에 기반한 픽셀 단위 분할 방법을 제안했습니다.

**Nilsson et al. [4] proposed to segment pigs from image by a structured prediction approach with several extracted image features.**  
Nilsson 등 [4]은 다양한 이미지 특징을 추출한 뒤, 구조적 예측 접근법으로 돼지를 분할하는 방법을 제안했습니다.

**Nasirahmadi et al. [3] described depth sensor based imaging systems along with 2D cameras for effectively identifying livestock behaviours, and presented automatic approach for monitoring cattles and pigs.**  
Nasirahmadi 등 [3]은 2D 카메라와 깊이 센서를 활용한 영상 시스템을 통해 가축의 행동을 효과적으로 식별하고, 소와 돼지를 자동으로 모니터링하는 방법을 제안했습니다.

**Most segmentation methods mentioned above segment pigs or other farmed animals with sensor-based or traditional machine learning techniques.**  
위에 언급된 대부분의 분할 방법은 센서 기반 또는 전통적인 머신러닝 기법을 이용하여 돼지나 기타 가축을 분할합니다.

<br>

**Recenlty, CNN based methods [5], [6], [8], [9], [13], [14] have been proposed to study the behavior of animals.**  
최근에는 동물의 행동을 연구하기 위해 CNN 기반의 방법 [5], [6], [8], [9], [13], [14]이 제안되었습니다.

**Cowton et al. [5] combined Faster R-CNN with two potential real-time multi-object tracking methods to autonomously localise and track individual pigs from RGB cameras.**  
Cowton 등 [5]은 Faster R-CNN과 두 가지 실시간 다중 객체 추적 기법을 결합하여 RGB 카메라로 개별 돼지를 자동으로 추적했습니다.

**Tian et al. [9] proposed a deep learning solution to address the pig counting problem by modifying counting convolutional neural network model according to the structure of ResNeXt [15].**  
Tian 등 [9]은 ResNeXt 구조를 기반으로 카운팅 CNN 모델을 수정하여 돼지 수를 세는 문제를 해결하는 딥러닝 솔루션을 제안했습니다.

**The proposed CNN model learns the mapping from the image features to the density map, and obtains the total number of pigs in the entire image by integrating the density map.**  
제안된 CNN 모델은 이미지 특징을 밀도 맵으로 매핑하는 학습을 수행하며, 이를 통합하여 전체 이미지의 돼지 수를 계산합니다.

**Zhang et al. [8] proposed a CNN-based detector and a correlation filter-based tracker via a hierarchical data association algorithm to multiple pigs detection and tracking.**  
Zhang 등 [8]은 계층적 데이터 연관 알고리즘을 통해 다수의 돼지를 탐지하고 추적하기 위한 CNN 기반 탐지기와 상관 필터 기반 추적기를 제안했습니다.

**Yang et al. [13] used Faster R-CNN to locate and identify individual pig.**  
Yang 등 [13]은 Faster R-CNN을 활용하여 개별 돼지를 탐지하고 식별했습니다.

**Zheng et al. [6] introduced Faster R-CNN framework to identify five postures and obtain sows accurate location in loose pens.**  
Zheng 등 [6]은 Faster R-CNN을 사용하여 헛간 안에서의 암퇘지 자세 다섯 가지를 식별하고 정확한 위치를 추정하는 방법을 제안했습니다.

**Hansen et al. [14] used Fisherface and CNN model for pig face recognition.**  
Hansen 등 [14]은 Fisherface와 CNN 모델을 이용한 돼지 얼굴 인식 방법을 사용했습니다.

---

**Generally, current deep learning based segmentation methods can be roughly categorized into two classes.**  
일반적으로, 현재의 딥러닝 기반 분할 방법은 두 가지로 구분될 수 있습니다.

**One is detection based segmentation methods [16]–[18] and the other is direct segmentation methods [19]–[25].**  
하나는 탐지 기반 분할 방법 [16]–[18], 다른 하나는 직접 분할 방법 [19]–[25]입니다.

**Detection based methods first obtain the region of each instance, and then predict the mask for each region.**  
탐지 기반 방법은 먼저 각 인스턴스의 영역을 찾고, 이후 해당 영역에 대해 마스크를 예측합니다.

**Direct segmentation methods predict the label of each pixel to form instance segmentation results directly.**  
직접 분할 방법은 각 픽셀의 레이블을 바로 예측하여 인스턴스 분할 결과를 생성합니다.

---

**B. DETECTION BASED SEGMENTATION METHODS**  
**B. 탐지 기반 분할 방법**

**The Region-based Convolutional Neural Network method (RCNN) [26] achieved excellent object detection accuracy by using a deep ConvNet to classify object proposals.**  
RCNN [26]은 깊은 ConvNet을 활용해 객체 후보를 분류함으로써 뛰어난 객체 탐지 정확도를 달성했습니다.

**Then, Ross Girshick [27] proposed a Fast-RCNN for object detection.**  
이후 Ross Girshick [27]은 객체 탐지를 위한 Fast-RCNN을 제안했습니다.

**Based on Fast-RCNN, Ren et al. [28] proposed Faster-RCNN method by combining a region proposal network with Fast-RCNN into a single network by sharing their convolutional features.**  
Fast-RCNN을 기반으로, Ren 등 [28]은 영역 제안 네트워크를 Fast-RCNN과 통합하여 합성곱 특징을 공유하는 Faster-RCNN을 제안했습니다.

**These methods just focus on object detection.**  
이들 방법은 객체 탐지에만 집중합니다.

**Mask-RCNN [16], as an effective detect-then-segment methodology, is a very successful instantiation.**  
Mask-RCNN [16]은 탐지 후 분할 방식의 성공적인 사례입니다.

**Mask-RCNN extends Faster-RCNN by adding a branch for predicting segmentation masks on each Region of Interest (RoI).**  
Mask-RCNN은 Faster-RCNN에 각 관심 영역(RoI)에 대한 분할 마스크를 예측하는 분기를 추가하여 확장한 것입니다.

**Chen et al. [17] proposed MaskLab by using position sensitive scores for object segmentation.**  
Chen 등 [17]은 위치 민감 점수를 활용한 객체 분할 방법인 MaskLab을 제안했습니다.

**Huang et al. [18] proposed Mask Scoring RCNN to learn the quality of the predicted instance masks with a network block.**  
Huang 등 [18]은 예측된 인스턴스 마스크의 품질을 학습하는 네트워크 블록인 Mask Scoring RCNN을 제안했습니다.

**Chen et al. [29] proposed TensorMask framework by establishing the first dense sliding window instance segmentation system.**  
Chen 등 [29]은 최초의 조밀한 슬라이딩 윈도우 기반 인스턴스 분할 시스템인 TensorMask 프레임워크를 제안했습니다.

**However, an underlying drawback in these methods is that mask quality depends on the classification scores.**  
하지만 이들 방법의 근본적인 문제는 마스크 품질이 분류 점수에 의존한다는 점입니다.

**It is inappropriate to use classification confidence to evaluate the mask quality.**  
분류 신뢰도를 마스크 품질 평가에 사용하는 것은 적절하지 않습니다.

---

**C. DIRECT SEGMENTATION METHODS**  
**C. 직접 분할 방법**

**Recently, the direct segmentation methods without depending on the detected bounding box have drawn lots of attentions, such as FCNs [30], SegNet [31], and Unet [19].**  
최근에는 탐지된 바운딩 박스에 의존하지 않고 직접 분할을 수행하는 FCN [30], SegNet [31], Unet [19] 등이 주목받고 있습니다.

**These approaches can produce pixel-wise dense prediction by an encoder-decoder architecture.**  
이러한 접근법은 인코더-디코더 구조를 통해 픽셀 단위의 조밀한 예측을 생성할 수 있습니다.

**Generally, an encoder-decoder architecture consists of a contracting (encoder) and expanding (decoder) sub-network.**  
일반적으로 인코더-디코더 구조는 축소 네트워크(인코더)와 확장 네트워크(디코더)로 구성됩니다.

**The encoder captures global context, while the decoder fuses global info with local details to generate segmentation.**  
인코더는 전체 이미지의 전역 맥락을 포착하고, 디코더는 전역 정보와 지역 정보를 결합하여 분할을 생성합니다.

**Unet can handle data scarcity and class imbalance, and can be extended to other computer vision tasks.**  
Unet은 데이터 부족, 클래스 불균형 문제를 해결할 수 있으며 다른 비전 작업에도 적용할 수 있습니다.

**However, Unet only uses the original image and ignores context guidance and multi-scale info.**  
하지만 Unet은 원본 이미지만 사용하며, 맥락 정보나 다중 스케일 정보를 활용하지 않습니다.

<br>

**Different Unet variants [20]–[25] have been proposed for better segmentation.**  
더 나은 분할을 위해 다양한 Unet 변형 [20]–[25]이 제안되었습니다.

**Multi-scale information has been shown to improve performance.**  
다중 스케일 정보는 분할 성능 향상에 효과적인 것으로 밝혀졌습니다.

**Yang et al. [23] proposed CLCINet, a cross-level fusion and context inference network.**  
Yang 등 [23]은 레벨 간 융합과 문맥 추론을 수행하는 CLCINet을 제안했습니다.

**Zhou et al. [24] proposed D-UNet, fusing 2D and 3D convolutions in encoding.**  
Zhou 등 [24]은 인코딩 단계에서 2D와 3D 합성곱을 융합한 D-UNet을 제안했습니다.

**Qi et al. [25] proposed X-Net using depthwise separable convolution and a feature similarity module.**  
Qi 등 [25]은 깊이 분리 합성곱과 특징 유사성 모듈을 사용하는 X-Net을 제안했습니다.

---

**There is a large demand for intelligent farming of chickens and pigs.**  
닭과 돼지를 위한 지능형 농업에 대한 수요가 큽니다.

**Though some pig segmentation methods exist, chicken segmentation is less explored.**  
일부 돼지 분할 기법이 존재하지만 닭에 대한 자동 분할과 분석은 거의 연구되지 않았습니다.

**Chicken segmentation is more challenging due to its small size and flocking behavior.**  
닭은 크기가 작고 군집 행동을 하기에 분할이 더 어렵습니다.

**In this work, we propose an automatic deep network framework for effective chicken image segmentation.**  
이에 본 연구에서는 효과적인 닭 이미지 분할을 위한 자동 딥 네트워크 프레임워크를 제안합니다.

---

![image](https://github.com/user-attachments/assets/44297658-d998-4d0d-8e70-b981cf07c7c0)

> - **Otsu 분할** : Otsu는 이미지를 두 그룹으로 나누기 위해, **가장 잘 구분되는(클래스 간 분산이 가장 큰) 임계값**을 자동으로 계산해주는 이진화 방법

> - **가우시안 혼합(GMM)** : 데이터가 여러 개의 **정규분포(가우시안 분포)** 로 구성되어 있다고 가정하고, 각 분포를 찾아내어 전체 분포를 모델링하는 방법

> - **엔트로피 기반 임계값** : 픽셀 분포의 정보량(엔트로피)을 기준으로, **전체 엔트로피가 최대가 되는 지점**을 임계값으로 설정하는 방법. 배경과 객체가 서로 가장 구별되도록 정보를 분리하려는 목적을 가짐

> - **스펙트럼 반사 분석** : 물체의 **재질 고유의 빛 반사 특성(스펙트럼 반사율)** 을 분석하여 물체를 구분하는 기법. 특정 파장대의 반사 특성을 이용해 동일한 색상이라도 재질이 다르면 구분 가능함 (예: 적외선/근적외선 영상 등에서 사용)

---

![image](https://github.com/user-attachments/assets/fc6b31af-14a6-47bf-89ee-8770e5ffdad3)

> - **R-CNN (Region-based CNN)** :  입력 이미지에서 **Selective Search**로 수천 개의 후보 영역(region proposal)을 생성하고, 각 영역을 잘라서 CNN에 통과시켜 특징을 추출하고 SVM으로 분류하는 방식.  
>   → CNN 기반의 첫 객체 탐지 모델  
>   → 단점 : 속도가 매우 느림 (각 영역을 **하나씩 CNN에 입력**)

> - **Fast R-CNN** : 전체 이미지를 CNN에 **한 번만 통과시켜 feature map 생성**, 이후 후보 영역(ROI)을 feature map에서 잘라내어 분류하고 위치를 보정함.  
>   → **R-CNN보다 훨씬 빠름**  
>   → 발전한 점 : 이미지 전체에 대해 CNN **1회만 수행**, ROI Pooling 도입

> - **Faster R-CNN** : 후보 영역을 외부 알고리즘 없이, CNN 안에서 자동으로 생성하는 **Region Proposal Network (RPN)**을 도입  
>   → **Fast R-CNN의 병목이었던 Selective Search를 제거**  
>   → 발전한 점 : 제안 영역 생성까지 **네트워크 내부에서 통합**, 전체가 **엔드투엔드(end-to-end) 학습 가능**

> - **Mask R-CNN** : Faster R-CNN에 **픽셀 단위 마스크 분할(segmentation mask)** 기능을 추가하여, 객체의 위치뿐 아니라 **정확한 윤곽까지 예측**  
>   → 발전한 점 : **객체 인스턴스 분할(instance segmentation)** 가능  
>   → ROI Pooling 대신 더 정확한 **ROI Align** 사용

---

> - **FCN (Fully Convolutional Network)** : 전통적인 CNN에서 완전 연결층(FC layer)을 제거하고, **모든 계층을 컨볼루션과 업샘플링으로만 구성**한 첫 번째 시맨틱 분할 네트워크.  
>   → 입력과 출력의 공간 구조를 유지하며 **픽셀 단위 예측** 가능  
>   → **기초 모델**로, 이후 많은 분할 네트워크의 기반이 됨

> - **SegNet** : FCN 구조에서 업샘플링을 개선한 구조로, **디코더에서 풀링 인덱스를 재사용**하여 더 정확하게 복원함.  
>   → 풀링 시 저장한 인덱스를 디코더 업샘플링에 그대로 사용  
>   → **FCN 대비 발전한 점** : **업샘플링 정확도 향상**, 계산량 절감

> - **U-Net** : FCN 구조에 **대칭적인 인코더-디코더 구조**와 **스킵 연결(skip connection)**을 도입하여 저해상도에서 손실된 정보를 복원  
>   → 생물 의학 영상 분할에서 매우 뛰어난 성능  
>   → **SegNet 대비 발전한 점** : **스킵 연결 도입**, **경계 정보 보존 강화**, **소량 데이터 대응력 우수**

> - **CLCI-Net (Cross-Level Context Integration Network)** : 다양한 수준의 특징을 통합하여 정밀한 경계를 추출하는 네트워크  
>   → **저수준 정보(자세한 경계)**와 **고수준 정보(의미적 의미)**를 결합하여 **정확도 향상**  
>   → **U-Net 대비 발전한 점** : **다중 레벨 특징 융합(Cross-Level Context)**, **경계 세분화 정밀도 향상**

> - **D-UNet (Dilated U-Net)** : U-Net에 **팽창합성곱(Dilated Convolution)** 을 적용하여, **수용영역을 확장**하면서도 해상도 손실 없이 특징을 추출  
>   → 더 넓은 문맥 정보를 활용해 분할 성능 향상  
>   → **U-Net 대비 발전한 점** : **팽창합성곱을 통한 문맥 강화**, **넓은 범위 컨텍스트 수용**

> - **X-Net** : U-Net 구조에서 **중간 디코더를 추가로 삽입**하여 다중 디코딩 경로를 갖는 확장 구조  
>   → 여러 해상도에서 예측 결과를 조합하여 **더 정밀한 분할** 가능  
>   → **U-Net 대비 발전한 점** : **다중 디코더 구조**, **피드백 정보 활용 강화**




