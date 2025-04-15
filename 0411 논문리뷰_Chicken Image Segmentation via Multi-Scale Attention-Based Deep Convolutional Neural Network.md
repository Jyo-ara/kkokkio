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
그 다음, 어텐션(attention) 기반 모듈을 사용해 유효한 특징을 추출하고 강조함으로써, 더 나은 분할 결과를 얻을 수 있습니다.

**Finally, a multi-output combined loss function is proposed to make effective supervision for better segmentation.**  
마지막으로, 더 나은 분할을 위한 효과적인 학습 지도를 위해 다중 출력 결합 손실 함수가 제안됩니다.

**Experimental results demonstrate the promising performance of the proposed framework for chicken image segmentation.**  
실험 결과는 제안된 프레임워크가 닭 이미지 분할에서 유망한 성능을 보임을 보여줍니다.

---

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
이러한 문제를 해결하기 위해, 우리는 효과적인 닭 이미지 분할을 위한 다중 스케일 어텐션 기반 딥 네트워크인 **MSAnet**을 제안합니다.

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
  보다 정확한 분할 성능을 위해, 채널 어텐션와 에지 어텐션를 포함하는 어텐션 기반 전략을 제안하여 효과적인 특징 추출을 수행합니다.

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
>   → **R-CNN 대비 발전한 점** : 이미지 전체에 대해 CNN **1회만 수행**, ROI Pooling 도입

> - **Faster R-CNN** : 후보 영역을 외부 알고리즘 없이, CNN 안에서 자동으로 생성하는 **Region Proposal Network (RPN)**을 도입  
>   → **Fast R-CNN의 병목이었던 Selective Search를 제거**  
>   → **Fast R-CNN 대비 발전한 점** : 제안 영역 생성까지 **네트워크 내부에서 통합**, 전체가 **엔드투엔드(end-to-end) 학습 가능**

> - **Mask R-CNN** : Faster R-CNN에 **픽셀 단위 마스크 분할(segmentation mask)** 기능을 추가하여, 객체의 위치뿐 아니라 **정확한 윤곽까지 예측**  
>   → **객체 인스턴스 분할(instance segmentation)** 가능  
>   → **Faster R-CNN 대비 발전한 점** : ROI Pooling 대신 더 정확한 **ROI Align** 사용

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
>   → **저수준 정보(자세한 경계)** 와 **고수준 정보(의미적 의미)** 를 결합하여 **정확도 향상**  
>   → **U-Net 대비 발전한 점** : **다중 레벨 특징 융합(Cross-Level Context)**, **경계 세분화 정밀도 향상**

> - **D-UNet (Dilated U-Net)** : U-Net에 **팽창합성곱(Dilated Convolution)** 을 적용하여, **수용영역을 확장**하면서도 해상도 손실 없이 특징을 추출  
>   → 더 넓은 문맥 정보를 활용해 분할 성능 향상  
>   → **U-Net 대비 발전한 점** : **팽창합성곱을 통한 문맥 강화**, **넓은 범위 컨텍스트 수용**

> - **X-Net** : U-Net 구조에서 **중간 디코더를 추가로 삽입**하여 다중 디코딩 경로를 갖는 확장 구조  
>   → 여러 해상도에서 예측 결과를 조합하여 **더 정밀한 분할** 가능  
>   → **U-Net 대비 발전한 점** : **다중 디코더 구조**, **피드백 정보 활용 강화**

---
---

## **III. METHODOLOGY 방법론**

**In this part, we introduce the proposed multi-scale attention based MSAnet method for chicken segmentation.**  
이 장에서는 닭 이미지 분할을 위한 제안된 다중 스케일 어텐션 기반 **MSAnet** 방법을 소개합니다.

**Fig. 3 illustrates the flowchart of our MSAnet segmentation method.**  
Fig. 3은 제안된 MSAnet 분할 방법의 전체 흐름도를 보여줍니다.
<p align="center">
    <img src="https://github.com/user-attachments/assets/5fe9cf46-b5ac-4c61-85fd-bb090ef2aff7" alt="image" width="700">
</p>

**The proposed method is an end-to-end deep network with four main parts.**  
제안된 방법은 네 가지 주요 구성 요소로 이루어진 엔드-투-엔드 딥 네트워크입니다.

**First, the MSAnet framework is an encoder-decoder structure network, which aims to learn effective hierarchical representation.**  
첫째, MSAnet은 인코더-디코더 구조의 네트워크로, 효과적인 계층적 표현 학습을 목표로 합니다.

**Second, we use a multi-scale module to construct an image pyramid input and achieve multi-level receptive field fusion for effective feature extraction.**  
둘째, 다중 스케일 모듈을 사용하여 이미지 피라미드를 입력으로 구성하고, 다단계 수용 영역 융합을 통해 효과적인 특징 추출을 수행합니다.

**Then the double attention module composed of channel attention and edge attention, can obtain global and local information for segmentation.**  
셋째, 채널 어텐션와 에지 어텐션로 구성된 이중 어텐션 모듈은 분할을 위한 전역 및 지역 정보를 동시에 획득할 수 있습니다.

**Last, the combined loss based on multi-scale side-outputs is utilized to provide effective supervision.**  
마지막으로, 다중 스케일 사이드 출력에 기반한 결합 손실 함수를 사용하여 효과적인 학습 지도를 제공합니다.

**The details of our MSAnet are illustrated as follows.**  
다음에서 MSAnet의 세부 내용을 설명합니다.

---
---

### **A. ENCODER-DECODER STRUCTURE NETWORK**  
**A. 인코더-디코더 구조 네트워크**

**As shown in Fig. 3, the proposed MSAnet framework is an end-to-end U-shape network composed by an encoder part and a decoder part.**  
**Fig. 3**에서 볼 수 있듯이, 제안된 MSAnet 프레임워크는 인코더와 디코더로 구성된 엔드-투-엔드 U자형 네트워크입니다.

**The encoder part performs convolution layer with a filter bank to produce a set of encoder feature maps,**  
인코더 부분은 필터 뱅크와 합성곱 계층을 통해 인코더 특징 맵을 생성합니다.

**while the decoder part utilizes up-sampling and feature enhancement operations to output feature maps for effective image segmentation.**  
반면 디코더 부분은 업샘플링과 특징 강화 연산을 이용하여 효과적인 이미지 분할을 위한 출력 특징 맵을 생성합니다.

---
---

### **B. MULTI-SCALE MODULE**  
**B. 다중 스케일 모듈**


**To deal with the various scales of chickens, we utilize multi-scale module for chicken segmentation by constructing a multi-scale input in the encoder path.**  
닭의 다양한 크기를 처리하기 위해, 인코더 경로에서 다중 스케일 입력을 구성하여 다중 스케일 모듈을 적용합니다.

**The multi-scale module has been proved effectively for image segmentation in work [21].**  
이 다중 스케일 모듈은 이미지 분할에서 효과적인 것으로 [21]에서 입증되었습니다.

**As shown in Fig. 3, two kinds of features can be integrated both from the vertical direction and horizontal direction for the $i^{\text{th}}$ layer of MSAnet, where $i \in [2, n]$.**  
**Fig. 3**에서 보이듯, MSAnet의 $i$번째 층에서는 수직 방향과 수평 방향 모두에서 특징을 통합할 수 있으며, $i \in [2, n]$입니다.

**The process for each layer can be described as**  
각 층의 처리 과정은 다음과 같이 정의됩니다:

<p align="center">
    <img src="https://github.com/user-attachments/assets/2e27c07c-66b3-4c0f-9896-6e3aef94b1af" alt="image" width="400">
</p>

---

**where $I$ denotes the original chicken image, and $I_i$ denotes the $i$-th down-sampled image of $I$. $n$ is the total layer number.**  
여기서 $I$는 원본 닭 이미지, $I_i$는 $I$의 $i$번째 다운샘플링 이미지이며, $n$은 총 층 수를 의미합니다.

**The function $\mathrm{Cat}(.)$ denotes the concatenate operation in the channel direction.**  
$\mathrm{Cat}(.)$ 함수는 채널 방향으로의 연결(concatenate) 연산을 의미합니다.

**$\mathrm{CR}(.)$ denotes one (Conv+ReLU) layer for feature extraction while $\mathrm{CR2}(.)$ denotes two (Conv+ReLU) layers.**  
$\mathrm{CR}(.)$는 특징 추출을 위한 하나의 Conv+ReLU 계층을, $\mathrm{CR2}(.)$는 두 개의 Conv+ReLU 계층을 의미합니다.

**$F_{v}^{i-1}$ denotes the features obtained from the $(i-1)$-th layer in the vertical direction as shown in Fig. 3.**  
$F_{v}^{i-1}$는 Fig. 3에서 보이듯 수직 방향으로 $(i-1)$번째 층에서 얻어진 특징을 의미합니다.

**$F_i$ is the extracted feature maps of the $i$-th layer which will be fed into the corresponding attention process as shown in Fig. 3.**  
$F_i$는 $i$번째 층에서 추출된 특징 맵이며, Fig. 3에 나타난 해당 attention 모듈로 입력됩니다.

---

**The multi-scale module has the following advantages for chicken segmentation:**  
다중 스케일 모듈은 닭 이미지 분할에 대해 다음과 같은 이점을 가집니다:

**1) dealing with various appearance generated by fast-growing process of chicken and making the scheme robust to different scales;**  
1\) 닭의 빠른 성장 과정에서 발생하는 다양한 외형을 처리하고, 다양한 크기에 대해 강건한 구조를 제공합니다.

**2) light-weight parameters by integrating multi-scale images into the decoder layers to alleviate the large growth of parameters;**  
2) 디코더 층에 다중 스케일 이미지를 통합함으로써, 파라미터 수의 급증을 완화하는 경량 구조를 구현합니다.

**3) providing effective information for better feature extraction and network supervision with side-outputs**  
3) 사이드 출력을 통해 더 나은 특징 추출과 네트워크 학습 감독을 위한 효과적인 정보를 제공합니다.

---
---

## **C. ATTENTION MECHANISM  어텐션 메커니즘**

**Recently attention mechanism has demonstrated its promising performance in many tasks [34]–[37].**  
최근 어텐션 메커니즘은 다양한 작업에서 뛰어난 성능을 보여주고 있습니다 [34]–[37].

**It is challenging to segment each chicken accurately from the occluded regions due to the similar appearances of grouped chickens.**  
무리지어 있는 닭들의 유사한 외형 때문에, 가려진 영역에서 개별 닭을 정확히 분할하는 것은 매우 어렵습니다.

**To address this problem, a double attention strategy, which contains channel attention for global enhancement and edge attention for edge details enhancement, is proposed in this paper.**  
이 문제를 해결하기 위해 본 논문에서는 전역 특징 강화를 위한 채널 어텐션(channel attention)과 경계선 세부정보 강화를 위한 엣지 어텐션(edge attention)으로 구성된 이중 어텐션 전략을 제안합니다.

**The details of the attention mechanism are introduced as below.**  
어텐션 메커니즘의 세부 내용은 다음과 같습니다.

---

### **Channel attention**  
**채널 어텐션**


**In order to make the network focus on more informative features, we propose to use the channel attention to generate different attention for each channel-wise feature.**  
네트워크가 더 유의미한 특징에 집중할 수 있도록, 각 채널마다 서로 다른 어텐션을 생성하는 채널 어텐션 방식을 제안합니다.

**Suppose that a feature $f$ with size of $(c \times h \times w)$ is the input, the channel attention module first converts $f$ to three components $X_f$, $Y_f$ and $Z_f$ via convolution operations $X(\cdot)$, $Y(\cdot)$ and $Z(\cdot)$, respectively.**  
크기가 $(c \times h \times w)$인 특징 맵 $f$가 입력이라고 가정하면, 채널 어텐션 모듈은 합성곱 연산 $X(\cdot)$, $Y(\cdot)$, $Z(\cdot)$을 통해 $f$를 $X_f$, $Y_f$, $Z_f$로 변환합니다.

$$
\begin{aligned}
X_f &= X(f), \\
Y_f &= Y(f), \\
Z_f &= Z(f)
\end{aligned}
\quad (2)
$$


**The tensor $Y_f'$ and $Z_f'$ are obtained by conducting reshape operation for tensor $Y_f$ and $Z_f$ respectively.**  
$Y_f'$와 $Z_f'$는 각각 $Y_f$와 $Z_f$에 리쉐이프 연산을 적용하여 얻습니다.

**The sizes of the tensors $X_f$, $Y_f'$ and $Z_f'$ are $(c \times h \times w)$, $(c \times hw)$ and $(hw \times c)$, respectively.**  
각 텐서의 크기는 $X_f$: $(c \times h \times w)$, $Y_f'$: $(c \times hw)$, $Z_f'$: $(hw \times c)$입니다.

**$X(\cdot)$ contains $\alpha$ convolutional layers which can be regarded as data preprocessing.**  
$X(\cdot)$는 $\alpha$개의 합성곱 계층으로 구성되며, 이는 데이터 전처리로 볼 수 있습니다.

**$Y(\cdot)$ and $Z(\cdot)$ are convolution operations, and the numbers of the convolutional layers are $\beta$ and $\gamma$, respectively.**  
$Y(\cdot)$와 $Z(\cdot)$는 각각 $\beta$, $\gamma$개의 합성곱 계층을 가진 연산입니다.

**$M$ is obtained by the matrix multiplication between $Y_f'$ and $Z_f'$, then fed into a softmax operation to regress channel attention weights $\theta$.**  
$M$은 $Y_f'$와 $Z_f'$의 행렬 곱으로 계산되며, 소프트맥스 연산을 통해 채널 어텐션 가중치 $\theta$를 생성합니다.

**$X_f$ and $\theta$ are dot-producted to obtain the final feature map $f_{CA}$.**  
$X_f$와 $\theta$는 내적되어 최종 어텐션 출력 특징 맵 $f_{CA}$를 생성합니다.

---

<p align="center">
    <img src="https://github.com/user-attachments/assets/92f5c043-4ce4-4acb-956b-5e3d38947562" alt="image" width="700">
</p>

**FIGURE 4. Pipeline of channel attention.**  
**그림 4. 채널 어텐션의 처리 파이프라인.**

**Feature map *f* is the input data.**  
특징 맵 *f*는 입력 데이터입니다.

**The blue blocks denote convolutional operations followed with *X(·)*, *Y(·)* and *Z(·)* operation respectively,**  
파란색 블록은 각각 *X(·)*, *Y(·)*, *Z(·)* 연산이 적용된 합성곱 연산을 나타냅니다.

**and the** $f_{\mathrm{CA}}$ **is the output result of channel attention.**  
그리고 $f_{\mathrm{CA}}$는 채널 어텐션의 출력 결과입니다.

--- 

**Fig. 4 shows the pipeline of channel attention and it can be defined as following:**  
Fig. 4는 채널 어텐션의 파이프라인을 보여주며, 다음과 같이 정의할 수 있습니다:

$$
\begin{aligned}
M &= Y_f' \odot Z_f', \\
\theta &= \text{softmax}(M), \\
f_{CA} &= \theta \odot X_f
\end{aligned}
\quad (3)
$$

**where $\odot$ is dot-producted operation.**  
여기서 $\odot$는 내적(dot-product) 연산을 의미합니다.

**The channel attention aims to enhance the channels with learned weight parameters $\theta$ in a global manner.**  
채널 어텐션은 학습된 가중치 $\theta$를 사용하여 전역적으로 채널을 강화하는 것을 목표로 합니다.

**For the channel attention, we empirically set the parameters $\alpha$, $\beta$ and $\gamma$ to 1, and we set 64 channels with $3 \times 3$ kernel sizes.**  
채널 어텐션에서는 $\alpha$, $\beta$, $\gamma$를 모두 1로 설정하고, $3 \times 3$ 커널 크기를 가진 64채널을 사용했습니다.

**The effectiveness of the proposed channel attention is demonstrated in the experiment section.**  
제안된 채널 어텐션의 효과는 실험 섹션에서 입증됩니다.

---

### **Edge attention**  
**엣지 어텐션**

**Inspired by [38], [39], we propose to use edge attention to recover detailed edge information.**  
[38], [39]에서 영감을 받아, 우리는 정밀한 경계 정보를 복원하기 위해 엣지 어텐션을 사용합니다.

**Edge attention seeks to exploit guided filter to extract edge detailed information from high-resolution images.**  
엣지 어텐션은 고해상도 이미지에서 정밀한 경계 정보를 추출하기 위해 가이드 필터를 활용합니다.

**Hence, high-quality segmentation results can be obtained from low-resolution poorly segmented results and precise segmented boundaries can be maintained after up-sampling.**  
따라서, 저해상도에서의 조악한 분할 결과도 고품질로 복원할 수 있으며, 업샘플링 후에도 정밀한 경계를 유지할 수 있습니다.

**Guided filter [38] is an edge-preserving image filter and has been incorporated into different deep learning tasks.**  
Guided filter [38]는 경계를 보존하는 이미지 필터로, 다양한 딥러닝 작업에 활용되어 왔습니다.

---

<p align="center">
    <img src="https://github.com/user-attachments/assets/a93a4283-ed00-4b1b-9eb2-6c7e652805dd" alt="image" width="700">
</p>

**FIGURE 5. Illustration of the edge attention.**  
**그림 5. 엣지 어텐션 구조도.**

**$F_l$ and $F_h$ are the low and high resolution features as the inputs of edge attention, and $T$ is the calculated attention map.**  
$F_l$과 $F_h$는 각각 저해상도 및 고해상도 특징 맵으로, 엣지 어텐션의 입력이며 $T$는 계산된 어텐션 맵입니다.

**The parameters of $W_h$ and $B_h$ can be obtained by $W_l$ and $B_l$ with up-sampling operations respectively.**  
$W_h$와 $B_h$의 파라미터는 각각 $W_l$과 $B_l$을 업샘플링하여 얻을 수 있습니다.

**The $F_h'$ is the final output of edge attention by linear operation with $W_h$, $B_h$, and $F_h$.**  
$F_h'$는 $W_h$, $B_h$, $F_h$를 이용한 선형 연산을 통해 생성된 엣지 어텐션의 최종 출력입니다.

---

**Fig. 5 shows the pipeline of edge attention (EA).**  
**Fig. 5**는 엣지 어텐션(EA)의 흐름도를 보여줍니다.

**Assume that feature map $F_l$ with the size of $(c \times h \times w)$ and feature map $F_h$ with size of $(c \times 2h \times 2w)$, the edge attention first takes $F_l$ and $F_h$ as input, the output is feature map $F_h'$ with the same size as $F_h$.**  
크기가 $(c \times h \times w)$인 $F_l$과 $(c \times 2h \times 2w)$인 $F_h$가 주어졌을 때, 엣지 어텐션은 이 둘을 입력으로 받아 $F_h$와 같은 크기의 출력 $F_h'$을 생성합니다.

---

**Edge attention first down-samples (bilinear) $F_h$ to the half of its scale to obtain feature $F_l'$ with size of $(c \times h \times w)$.**  
먼저 $F_h$를 이중선형 보간으로 다운샘플링하여 $(c \times h \times w)$ 크기의 특징 맵 $F_l'$을 얻습니다.

**Based on $F_l$ and $F_l'$, the attention map $T$ can be obtained as shown in Fig. 5.**  
$F_l$과 $F_l'$을 기반으로 어텐션 맵 $T$를 계산할 수 있으며, 이는 Fig. 5에 나타나 있습니다.

**Then the reconstruction error is minimized between $F_l$ and $F_l'$ to obtain the coefficients of the attention guided filter $W_l$ and $B_l$.**  
이후 $F_l$과 $F_l'$ 사이의 재구성 오차를 최소화하여 어텐션 가이드 필터 계수 $W_l$과 $B_l$을 구합니다.

**After that, the coefficients $W_h$ and $B_h$ can be obtained by up-sampling (bilinear) $W_l$ and $B_l$ to generate the final high-resolution output $F_h'$.**  
그 다음, $W_l$과 $B_l$을 이중선형 업샘플링하여 고해상도 출력 $F_h'$ 생성을 위한 계수 $W_h$, $B_h$를 얻습니다.

---

**Specifically, edge attention constructs a squared window $s_k$ with a radius $r$ for each position $k$ in the squared window.**  
엣지 어텐션은 각 위치 $k$에 대해 반지름 $r$을 갖는 정사각형 창 $s_k$를 구성합니다.

**Suppose that $F_{li}$ is a pixel of $F_l$, its output with respect to $s_k$ can be obtained by a linear transformation:**  
$F_{li}$가 $F_l$의 픽셀이라고 하면, $s_k$에 대한 출력은 다음과 같은 선형 변환으로 구할 수 있습니다:


<p align="center">
    <img src="https://github.com/user-attachments/assets/8c1f099a-1ef1-40b4-b08c-8088ad264c01" alt="image" width="400">
</p>

---

**where $w_k$ and $b_k$ are the linear coefficients of the window $s_k$.**  
여기서 $w_k$와 $b_k$는 창 $s_k$의 선형 계수입니다.

**The radius $r$ of the squared window is empirically set to 2 in this paper.**  
본 논문에서는 정사각형 창의 반지름 $r$을 2로 설정하였습니다.

---

**Based on the window, the difference between <img src="https://github.com/user-attachments/assets/43fafa7c-3216-44ab-adc0-669df87eccc0" width="70"/> for all the pixels in the window $s_k$ can be minimized to obtain the coefficients $(w_k, b_k)$ by Eq. 5:**  
$s_k$ 내의 모든 픽셀에 대해 <img src="https://github.com/user-attachments/assets/43fafa7c-3216-44ab-adc0-669df87eccc0" width="70"/> 사이의 차이를 최소화하여 계수 $(w_k, b_k)$를 다음과 같이 구합니다:

$$
\min_{w_k, b_k} E(w_k, b_k) =
\sum_{i \in s_k} \left( T_i^2 (w_k F_{l_i} + b_k - F'_{l_i})^2 + \lambda w_k^2 \right)
\quad (5)
$$


---

**where $\lambda$ is a regularization parameter which is empirically set to 0.02, and $T_i$ is the attention weight for position $i$.**  
여기서 $\lambda$는 실험적으로 0.02로 설정된 정규화 파라미터이며, $T_i$는 위치 $i$에 대한 어텐션 가중치입니다.

**The closed-form solution can be referred as:**  
이 문제의 **명시적 해 (closed-form solution)** 는 다음과 같습니다:

<p align="center">
    <img src="https://github.com/user-attachments/assets/38282f4a-6dd5-42de-b58f-ef2e9008c4ab" alt="image" width="400">
</p>

---

**$N_k$ is the number of the pixels in $w_k$**  
$N_k$는 윈도우 $w_k$ 안의 픽셀 수를 의미합니다.

**$X_i = \frac{T_i}{\sum_{i \in w_k} T_i}$**  
$X_i$는 윈도우 내 정규화된 어텐션 가중치입니다.

**and <img src="https://github.com/user-attachments/assets/bbe1f13f-06f9-4409-8227-8508e384497f" width="20"/> is the mean of $(\cdot)$, which is corresponding to the *Mean filter* described in Fig. 5.**  
그리고 <img src="https://github.com/user-attachments/assets/bbe1f13f-06f9-4409-8227-8508e384497f" width="20"/> 표기는 해당 항목의 평균을 의미하며, 이는 Fig. 5에 설명된 평균 필터와 대응됩니다.

---

**As each position $i$ is involved in multiple windows with different coefficients $w_k, b_k$,**  
각 위치 $i$는 서로 다른 계수 $w_k$, $b_k$를 갖는 여러 윈도우에 포함되므로,

**we average all the values of $\hat{F}_{ki}$ from different windows to generate $\hat{F}_i$,**  
다양한 윈도우로부터 계산된 $\hat{F}_{ki}$ 값들을 평균하여 최종 출력 $\hat{F}_i$를 생성합니다.

**which is equal to average the coefficients $(w_k, b_k)$ of all the windows overlapping $i$, as following:**  
이는 곧, $i$를 포함하는 모든 윈도우의 계수 $(w_k, b_k)$를 평균한 것과 동일합니다:

<p align="center">
    <img src="https://github.com/user-attachments/assets/33bfc53f-1385-41a9-b0e1-c500fe8a3df3" alt="image" width="400">
</p>

**which also can be represented as**  
이 식은 다음과 같이 표현될 수 있습니다:

$$
\hat{F}_i = W_l \ast F'_l + B_l \quad (7)
$$

---

**where $\Omega_i$ is the set of all the windows including the position $i$, and $\ast$ is the element-wise multiplication.**  
여기서 $\Omega_i$는 위치 $i$를 포함하는 모든 윈도우들의 집합이며, $\ast$는 원소별 곱셈 연산(element-wise multiplication)을 의미합니다.

**After up-sampling $W_l$ and $B_l$ to obtain $W_h$ and $B_h$, the final output is calculated by**  
$W_l$과 $B_l$을 업샘플링하여 $W_h$, $B_h$를 얻은 후, 최종 출력은 다음과 같이 계산됩니다:

$$
F'_h = W_h \ast F_h + B_h \quad (8)
$$

---

**The double attention module with channel attention and edge attention can guide the multi-scale network to extract more effective features for chicken segmentation.**  
채널 어텐션과 엣지 어텐션을 포함한 이중 어텐션 모듈은, 다중 스케일 네트워크가 닭 분할을 위해 보다 효과적인 특징을 추출하도록 유도할 수 있습니다.

**The flowchart of the proposed double attention module based network is shown in Fig. 3.**  
제안된 이중 어텐션 모듈 기반 네트워크의 흐름도는 Fig. 3에 나타나 있습니다.

---

### **Mask prediction and multi-scale side-outputs**  
**마스크 예측 및 다중 스케일 사이드 출력**

**The detailed pipeline of multi-scale side-outputs and combined loss are shown in Fig. 6.**  
다중 스케일 사이드 출력과 결합 손실의 세부 흐름은 Fig. 6에 제시되어 있습니다.

<p align="center">
    <img src="https://github.com/user-attachments/assets/d9e80883-8063-4475-84ef-3a12357c7bd3" alt="image" width="700">
</p>
그림 6. 다중 스케일 마스크 예측 및 결합 손실 처리 과정.

**To simplify, the main encoder-decoder part of the network is simply denoted as U shape which can be found in Fig. 3.**  
간단히 하기 위해, 네트워크의 주요 인코더-디코더 구조는 Fig. 3에 보이는 U-자 형태로 표현됩니다.

---

**As shown in Fig. 6, after obtaining features**  
Fig. 6에서 보이듯, 다음과 같은 특징을 추출한 뒤:

$$
F_{EA} = \{F_{EA_1}, ..., F_{EA_n}\}
$$

**returned by edge attention followed with convolutional and ReLU operations as the flowchart shown,**  
엣지 어텐션과 그 후의 합성곱 및 ReLU 연산을 거쳐 얻은 결과입니다.

---

**predicted multi-scale outputs**  
이후 예측된 다중 스케일 출력은 다음과 같습니다:

$$
M = \{M_1, ..., M_n\}
$$

**from multi-scale layers are obtained by corresponding mask prediction (MP) block, which can be formulated as following:**  
이 출력들은 각각의 마스크 예측 블록 $MP$를 통해 다음과 같이 계산됩니다:

$$
\begin{aligned}
M_1 &= MP(F_{EA_1}) \\
M_i &= MP(F_{EA_i}) \\
M_n &= MP(F_{EA_n})
\end{aligned}
\quad (9)
$$

---

**where $n$ is the total layer number.**  
여기서 $n$은 전체 층 수를 의미합니다.

**$MP(.)$ denotes mask prediction block which includes up-sample, convolutional and softmax operations.**  
$MP(.)$는 업샘플링, 합성곱, 소프트맥스 연산으로 구성된 마스크 예측 블록을 의미합니다.

**The side-output module is regarded as a classifier to produce a companion local output map for each layer by mask prediction operation.**  
사이드 출력 모듈은 각 층에 대해 마스크 예측 연산을 통해 지역적 보조 출력 맵을 생성하는 분류기로 간주됩니다.

---

### **D. COMBINED LOSS**  
**D. 결합 손실 함수**

**To conduct effective supervision for the network, we utilize the combined average loss of the multi-scale side-outputs for effective segmentation performance.**  
네트워크의 효과적인 학습을 위해, 다중 스케일 사이드 출력의 평균 손실을 결합한 형태로 사용하여 분할 성능을 향상시킵니다.

---

**For the $i^{\text{th}}$ layer, we can obtain the loss($i$) by negative log-likelihood loss**  
$i$번째 층에 대해, 음의 로그 가능도 손실(negative log-likelihood loss)을 통해 손실 값을 계산할 수 있습니다:

$$
\text{loss}(i) = -y \log(y_i) \quad (10)
$$

---

**where $y$ denotes the ground truth and $y_i$ is the predicted mask of the $i^{\text{th}}$ layer.**  
여기서 $y$는 정답 마스크(Ground truth), $y_i$는 $i$번째 층에서 예측된 마스크입니다.

---

**Then the combined loss of the network can be defined as following:**  
그 후, 전체 네트워크에 대한 결합 손실은 다음과 같이 정의됩니다:

$$
L = \sum_{i=1}^{n} \omega_i \cdot \text{loss}(i) \quad (11)
$$

---

**where $\omega_i$ is the loss weight for each side-output layer, and $n$ is the side-output number**  
여기서 $\omega_i$는 각 사이드 출력층에 대한 손실 가중치이며, $n$은 사이드 출력의 개수입니다.

**($\omega_i$ is set to 0.25, $n$ is set to 4 in our paper).**  
본 논문에서는 $\omega_i = 0.25$, $n = 4$로 설정하였습니다.

**$\text{loss}(i)$ denotes the loss of the $i^{\text{th}}$ side-output layer.**  
$\text{loss}(i)$는 $i$번째 사이드 출력층의 손실 값을 의미합니다.

---

**The process of multi-scale outputs and combined loss is demonstrated in Fig. 6,**  
다중 스케일 출력과 결합 손실 계산 과정은 Fig. 6에 설명되어 있습니다.

**where Conv+softmax denotes the convolutional (kernel size $1 \times 1$) and softmax operations.**  
여기서 Conv+softmax는 $1 \times 1$ 커널의 합성곱 연산과 softmax 연산을 의미합니다.

**Besides, bilinear interpolation method is used as up-sampling operation.**  
또한, 업샘플링 연산에는 이중선형 보간법(bilinear interpolation)이 사용됩니다.

---

**To utilize side-output segmentation maps effectively, the average map of all side-output maps is computed as the final segmentation result.**  
사이드 출력 분할 맵을 효과적으로 활용하기 위해, 모든 사이드 출력 맵의 평균을 최종 분할 결과로 사용합니다.

---
