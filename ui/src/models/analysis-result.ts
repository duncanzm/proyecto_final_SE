export class AnalysisResult {
  public speakerStatus: string;
  public failingFrecuencies: string[];

  constructor(speakerStatus: string, failingFrecuencies: string[]) {
    this.speakerStatus = speakerStatus;
    this.failingFrecuencies = failingFrecuencies;
  }
}
