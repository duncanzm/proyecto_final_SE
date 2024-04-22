import {Component, Input, OnInit} from '@angular/core';
import {NgForOf} from "@angular/common";
import {AnalysisResult} from "../../../../models/analysis-result";
import {SoundServiceService} from "../../../services/sound-service.service";
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { faCoffee } from '@fortawesome/free-solid-svg-icons';
import {faPlay} from "@fortawesome/free-solid-svg-icons/faPlay";

@Component({
  selector: 'app-measurement-error',
  standalone: true,
  imports: [
    NgForOf,
    FontAwesomeModule
  ],
  templateUrl: './measurement-error.component.html',
  styleUrl: './measurement-error.component.css'
})
export class MeasurementErrorComponent implements OnInit{
  protected readonly Number = Number;

  @Input()
  analysisResult: AnalysisResult | undefined;

  @Input()
  data: any | undefined;

  tableResults: { value: number | string; frequency: string }[] | undefined = [];
  faCoffee = faCoffee;


  constructor(private soundService: SoundServiceService) {
  }

  ngOnInit(): void {
    console.log(this.data)
    this.tableResults = this.analysisResult?.failingFrecuencies.map((value, index) => {
      return {
        frequency: value,
        value: this.data ? this.data[value] < 0 ? this.data[value] : "+" + this.data[value] : ''
      }
    });
  }

  generateSound(num:number){
    this.soundService.generateSineWave(num);
  }


  protected readonly faPlay = faPlay;
}
