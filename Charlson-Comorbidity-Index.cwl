cwlVersion: v1.0
steps:
  read-potential-cases-omop:
    run: read-potential-cases-omop.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule1
  charlson-comorbidity-index-any---primary:
    run: charlson-comorbidity-index-any---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule2
      potentialCases:
        id: potentialCases
        source: read-potential-cases-omop/output
  lymphoproliferative-charlson-comorbidity-index---primary:
    run: lymphoproliferative-charlson-comorbidity-index---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule3
      potentialCases:
        id: potentialCases
        source: charlson-comorbidity-index-any---primary/output
  pulmonary-charlson-comorbidity-index---primary:
    run: pulmonary-charlson-comorbidity-index---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule4
      potentialCases:
        id: potentialCases
        source: lymphoproliferative-charlson-comorbidity-index---primary/output
  cerebrovascular-charlson-comorbidity-index---primary:
    run: cerebrovascular-charlson-comorbidity-index---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule5
      potentialCases:
        id: potentialCases
        source: pulmonary-charlson-comorbidity-index---primary/output
  charlson-comorbidity-index-cardiac---primary:
    run: charlson-comorbidity-index-cardiac---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule6
      potentialCases:
        id: potentialCases
        source: cerebrovascular-charlson-comorbidity-index---primary/output
  charlson-comorbidity-index-hemiplegia---primary:
    run: charlson-comorbidity-index-hemiplegia---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule7
      potentialCases:
        id: potentialCases
        source: charlson-comorbidity-index-cardiac---primary/output
  charlson-comorbidity-index-complication---primary:
    run: charlson-comorbidity-index-complication---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule8
      potentialCases:
        id: potentialCases
        source: charlson-comorbidity-index-hemiplegia---primary/output
  charlson-comorbidity-index---primary:
    run: charlson-comorbidity-index---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule9
      potentialCases:
        id: potentialCases
        source: charlson-comorbidity-index-complication---primary/output
  charlson-comorbidity-index-tumour---primary:
    run: charlson-comorbidity-index-tumour---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule10
      potentialCases:
        id: potentialCases
        source: charlson-comorbidity-index---primary/output
  severe-charlson-comorbidity-index---primary:
    run: severe-charlson-comorbidity-index---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule11
      potentialCases:
        id: potentialCases
        source: charlson-comorbidity-index-tumour---primary/output
  charlson-comorbidity-index-liver---primary:
    run: charlson-comorbidity-index-liver---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule12
      potentialCases:
        id: potentialCases
        source: severe-charlson-comorbidity-index---primary/output
  charlson-comorbidity-index-dementium---primary:
    run: charlson-comorbidity-index-dementium---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule13
      potentialCases:
        id: potentialCases
        source: charlson-comorbidity-index-liver---primary/output
  output-cases:
    run: output-cases.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule14
      potentialCases:
        id: potentialCases
        source: charlson-comorbidity-index-dementium---primary/output
class: Workflow
inputs:
  inputModule1:
    id: inputModule1
    doc: Js implementation unit
    type: File
  inputModule2:
    id: inputModule2
    doc: Python implementation unit
    type: File
  inputModule3:
    id: inputModule3
    doc: Python implementation unit
    type: File
  inputModule4:
    id: inputModule4
    doc: Python implementation unit
    type: File
  inputModule5:
    id: inputModule5
    doc: Python implementation unit
    type: File
  inputModule6:
    id: inputModule6
    doc: Python implementation unit
    type: File
  inputModule7:
    id: inputModule7
    doc: Python implementation unit
    type: File
  inputModule8:
    id: inputModule8
    doc: Python implementation unit
    type: File
  inputModule9:
    id: inputModule9
    doc: Python implementation unit
    type: File
  inputModule10:
    id: inputModule10
    doc: Python implementation unit
    type: File
  inputModule11:
    id: inputModule11
    doc: Python implementation unit
    type: File
  inputModule12:
    id: inputModule12
    doc: Python implementation unit
    type: File
  inputModule13:
    id: inputModule13
    doc: Python implementation unit
    type: File
  inputModule14:
    id: inputModule14
    doc: Python implementation unit
    type: File
outputs:
  cases:
    id: cases
    type: File
    outputSource: output-cases/output
    outputBinding:
      glob: '*.csv'
requirements:
  SubworkflowFeatureRequirement: {}
