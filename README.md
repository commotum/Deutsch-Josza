# Deutsch-Josza


0      |               [PU]  ⇒  ∣DD⟩      |               [PU]  ⇒  ∣00⟩      |
1      |      ∣DD⟩  ⇒  [X1]  ⇒  ∣DC⟩      |      ∣00⟩  ⇒  [X1]  ⇒  ∣01⟩      |
2      |      ∣DC⟩  ⇒  [H0]  ⇒  ∣BC⟩      |      ∣01⟩  ⇒  [H0]  ⇒  ∣11⟩      |
3      |      ∣BC⟩  ⇒  [H1]  ⇒  ∣BC⟩      |      ∣11⟩  ⇒  [H1]  ⇒  ∣11⟩      |
4      |      ∣BC⟩  ⇒ [CX01] ⇒  ∣CD⟩      |      ∣11⟩  ⇒ [CX01] ⇒  ∣10⟩      |
5      |      ∣CD⟩  ⇒  [H0]  ⇒  ∣CD⟩      |      ∣10⟩  ⇒  [H0]  ⇒  ∣10⟩      |

      00        01        02        03        04        05
[PU] ∣DD⟩ [X1] ∣DC⟩ [H0] ∣BC⟩ [H1] ∣BC⟩ [CX] ∣CD⟩ [H0] ∣CD⟩
[PU] ∣00⟩ [X1] ∣01⟩ [H0] ∣11⟩ [H1] ∣11⟩ [CX] ∣10⟩ [H0] ∣10⟩ : [Balanced]




      00        01        02        03        04        05
[PU] ∣DD⟩ [X1] ∣DC⟩ [H0] ∣BC⟩ [H1] ∣BC⟩ [CX] ∣CD⟩ [H0] ∣CD⟩ : [Balanced]
[PU]  ⇒ ∣00⟩ ⇒ [X1] ⇒ ∣01⟩ ⇒ [H0] ⇒ ∣11⟩ ⇒ [H1] ⇒ ∣11⟩ ⇒ [CX] ⇒ ∣10⟩ ⇒ [H0] ⇒ ∣10⟩ : [Balanced]

  ⇒  0  ⇒  0  ⇒  0  ⇒  0  ⇒  0  ⇒  0  ⇒  
 

[PU] ∣DD⟩ ∣00⟩
[X1] ∣DC⟩ ∣01⟩
[H0] ∣BC⟩ ∣11⟩ 
[H1] ∣BC⟩ ∣11⟩ 
[CX] ∣CD⟩ ∣10⟩
[H0] ∣CD⟩ ∣10⟩

0    [PU] : ∣DD⟩ = ∣00⟩
1    [X1] : ∣DC⟩ = ∣01⟩
2    [H0] : ∣BC⟩ = ∣11⟩ 
3    [H1] : ∣BC⟩ = ∣11⟩ 
4    [CX] : ∣CD⟩ = ∣10⟩
5    [H0] : ∣CD⟩ = ∣10⟩

[PU]  :  ∣DD⟩  //  ∣00⟩
[X1]  :  ∣DC⟩  //  ∣01⟩
[H0]  :  ∣BC⟩  //  ∣11⟩ 
[H1]  :  ∣BC⟩  //  ∣11⟩ 
[CX]  :  ∣CD⟩  //  ∣10⟩
[H0]  :  ∣CD⟩  //  ∣10⟩

0    [PU]  ∣DD⟩  ∣00⟩
1    [X1]  ∣DC⟩  ∣01⟩
2    [H0]  ∣BC⟩  ∣11⟩ 
3    [H1]  ∣BC⟩  ∣11⟩ 
4    [CX]  ∣CD⟩  ∣10⟩
5    [H0]  ∣CD⟩  ∣10⟩

0    [PU]    ∣DD⟩    ∣00⟩
1    [X1]    ∣DC⟩    ∣01⟩
2    [H0]    ∣BC⟩    ∣11⟩ 
3    [H1]    ∣BC⟩    ∣11⟩ 
4    [CX]    ∣CD⟩    ∣10⟩
5    [H0]    ∣CD⟩    ∣10⟩

[PU]  :  ∣DD⟩  //  ∣00⟩
[X1]  :  ∣DC⟩  //  ∣01⟩
[H0]  :  ∣BC⟩  //  ∣11⟩ 
[H1]  :  ∣BC⟩  //  ∣11⟩ 
[CX]  :  ∣CD⟩  //  ∣10⟩
[H0]  :  ∣CD⟩  //  ∣10⟩




The Circuit is [Balanced].





 = ∣01⟩    [H(1)]
2    ∣BC⟩ = ∣11⟩    [H(0)]
3    ∣CD⟩ = ∣01⟩    [H(1)]

 = ∣00⟩



0 ∣10⟩ (m, n) = (D, D) (0, 0)
Step 1: (m, n) = (D, C) (0, 1)  [Balanced]
Step 2: (m, n) = (B, C)  ->  balance = (1, 1)  [Constant]
Step 3: (m, n) = (B, C)  ->  balance = (1, 1)  [Constant]
Step 4: (m, n) = (C, D)  ->  balance = (1, 0)  [Balanced]
Step 5: (m, n) = (C, D)  ->  balance = (1, 0)  [Balanced]