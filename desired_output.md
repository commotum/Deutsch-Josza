current output:

        00         01         02         03         04         05
 [PU] ∣AD⟩  [X1] ∣AC⟩  [H0] ∣AC⟩  [H1] ∣AC⟩ [CX01] ∣DC⟩  [H0] ∣BC⟩
 [PU] ∣00⟩  [X1] ∣01⟩  [H0] ∣01⟩  [H1] ∣01⟩ [CX01] ∣01⟩  [H0] ∣11⟩ : [Constant]

desired output:

      00        01        02        03          04        05
[PU] ∣DD⟩ [X1] ∣DC⟩ [H0] ∣BC⟩ [H1] ∣BC⟩ [CX01] ∣CD⟩ [H0] ∣CD⟩
[PU] ∣00⟩ [X1] ∣01⟩ [H0] ∣11⟩ [H1] ∣11⟩ [CX01] ∣10⟩ [H0] ∣10⟩ : [Balanced]


|-------|--------|-----------|-------|
| INPUT |        |           | INPUT |
| INPUT | OUTPUT | RECORD(F) | INPUT |
| INPUT | OUTPUT | RECORD(F) | INPUT |
| INPUT |        |           | INPUT |
|-------|--------|-----------|-------|
| INPUT | INPUT  | INPUT | INPUT |
|       | INPUT  | INPUT | INPUT |
|       |        | INPUT | INPUT |
|-------|--------|-------|-------|

|:---------------:|:---------------:|:----------------:|:---------------:|
|        A        |        B        |        C         |        D        |
|:---------------:|:---------------:|:----------------:|:---------------:|
|     INPUT       |        -        |        -         |        -        |
|     INPUT       |     OUTPUT      |   RECORD(F)      |        -        |
|     INPUT       |     OUTPUT      |   RECORD(F)      |     OUTPUT      |
|     INPUT       |        -        |        -         |     OUTPUT      |
|-----------------|-----------------|------------------|-----------------|
|     INPUT       |     INPUT       |  RECORD(F^(-1))  |     OUTPUT      |
|        -        |     INPUT       |  RECORD(F^(-1))  |     OUTPUT      |
|        -        |        -        |        -         |     OUTPUT      |
|:---------------:|:---------------:|:----------------:|:---------------:|


Table 3.2: Bennett’s method for making a computation reversible.

|--------|--------|------------|--------|
| INPUT  |  ----  |    ----    |  ----  |
| INPUT  | OUTPUT | RECORD(F)  |  ----  |
| INPUT  | OUTPUT | RECORD(F)  | OUTPUT |
| INPUT  |  ----  |    ----    | OUTPUT |
|--------|--------|------------|--------|
| INPUT  | INPUT  | RECORD(F⁻¹)| OUTPUT |
|  ----  | INPUT  | RECORD(F⁻¹)| OUTPUT |
|  ----  |  ----  |    ----    | OUTPUT |
|--------|--------|------------|--------|



