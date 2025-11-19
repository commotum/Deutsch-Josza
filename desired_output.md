current output:

        00         01         02         03         04         05
 [PU] ∣AD⟩  [X1] ∣AC⟩  [H0] ∣AC⟩  [H1] ∣AC⟩ [CX01] ∣DC⟩  [H0] ∣BC⟩
 [PU] ∣00⟩  [X1] ∣01⟩  [H0] ∣01⟩  [H1] ∣01⟩ [CX01] ∣01⟩  [H0] ∣11⟩ : [Constant]

desired output:

      00        01        02        03        04        05
[PU] ∣DD⟩ [X1] ∣DC⟩ [H0] ∣BC⟩ [H1] ∣BC⟩ [CX] ∣CD⟩ [H0] ∣CD⟩
[PU] ∣00⟩ [X1] ∣01⟩ [H0] ∣11⟩ [H1] ∣11⟩ [CX] ∣10⟩ [H0] ∣10⟩ : [Balanced]