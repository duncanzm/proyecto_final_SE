import {Component, Input, OnInit} from '@angular/core';
import {AnalysisResult} from "../../../../models/analysis-result";
import {NgForOf} from "@angular/common";
import {SoundServiceService} from "../../../services/sound-service.service";
import {faPlay} from "@fortawesome/free-solid-svg-icons/faPlay";
import {FaIconComponent} from "@fortawesome/angular-fontawesome";

@Component({
  selector: 'app-valid-monitor',
  standalone: true,
  imports: [
    NgForOf,
    FaIconComponent
  ],
  templateUrl: './valid-monitor.component.html',
  styleUrl: './valid-monitor.component.css'
})
export class ValidMonitorComponent implements OnInit{
  protected readonly Number = Number;

  @Input()
  analysisResult: AnalysisResult | undefined;

  @Input()
  data: any | undefined;

  tableResults: { value: number | string; frequency: string }[] = [];

  constructor(private soundService: SoundServiceService) {
  }

  ngOnInit(): void {
    for(let value of Object.keys(this.data)){
      // add row to tableResults
      this.tableResults.push({
        frequency: value,
        value: this.data ? this.data[value] < 0 ? this.data[value] : "+" + this.data[value] : ''
      });
    }
  }


  generateSound(num:number){
    this.soundService.generateSineWave(num);
  }

  protected readonly faPlay = faPlay;
}
