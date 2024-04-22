import {Component, Input, OnInit} from '@angular/core';
import {AnalysisResult} from "../../../../models/analysis-result";
import {NgForOf} from "@angular/common";
import {SoundServiceService} from "../../../services/sound-service.service";
import {faPlay} from "@fortawesome/free-solid-svg-icons/faPlay";
import {FaIconComponent} from "@fortawesome/angular-fontawesome";

@Component({
  selector: 'app-invalid-monitor',
  standalone: true,
  imports: [
    NgForOf,
    FaIconComponent
  ],
  templateUrl: './invalid-monitor.component.html',
  styleUrl: './invalid-monitor.component.css'
})
export class InvalidMonitorComponent implements OnInit{

  protected readonly Number = Number;

  @Input()
  analysisResult: AnalysisResult | undefined;

  @Input()
  data: any | undefined;

  tableResults: { value: number | string; frequency: string }[] | undefined = [];

  constructor(private soundService: SoundServiceService) {
  }

  ngOnInit(): void {
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



