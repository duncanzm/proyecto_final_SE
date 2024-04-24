import {Component, EventEmitter, Input, OnInit, Output, signal} from '@angular/core';
import Chart from 'chart.js/auto';
import {HttpClient} from "@angular/common/http";
import {InvalidMonitorComponent} from "./invalid-monitor/invalid-monitor.component";
import {ValidMonitorComponent} from "./valid-monitor/valid-monitor.component";
import {AnalysisResult} from "../../../models/analysis-result";
import {NgIf} from "@angular/common";
import {MeasurementErrorComponent} from "./measurement-error/measurement-error.component";
import {LoadingComponent} from "../shared/loading/loading.component";
import Swal from 'sweetalert2'


@Component({
  selector: 'app-equalizer',
  standalone: true,
  imports: [
    InvalidMonitorComponent,
    ValidMonitorComponent,
    NgIf,
    MeasurementErrorComponent,
    LoadingComponent
  ],
  templateUrl: './equalizer.component.html',
  styleUrl: './equalizer.component.css'
})
export class EqualizerComponent implements OnInit{


  public chart: any;
  @Input()
  data: any;

  @Input()
  rawData: any;

  analysisResult: AnalysisResult | undefined;

  @Output()
  resetEvent = new EventEmitter<void>();

  loading = false;

  constructor(private httpClient:HttpClient) {
  }

  ngOnInit(): void {
    this.loadData();
    this.createChart();
  }

  public createChart(){

    let keys = Object.keys(this.data);
    let values = Object.values(this.data).map(Number);
    let zeros = Array(keys.length).fill(0);
    let min = Math.min(...values) - 10;
    let max = Math.max(...values) + 10;

    this.chart = new Chart("frequencies", {
      type: 'line',

      data: {// values on X-Axis
        labels: keys,
        datasets: [
          {
            label: "dB",
            data: values,
            backgroundColor: "#3884de",
            borderColor: '#a8a8a8',
            borderWidth: 1.75,
            pointStyle: 'circle',
            pointRadius: 3.5,
            pointHoverRadius: 5,
            pointBackgroundColor: function(context) {
              var index = context.dataIndex;
              var value = context.dataset.data[index];
              // @ts-ignore
              return value === 0 ? 'green' : value < -5 || value > 5 ? 'red' : '#3884de';
            }
          },
          {
            label: "Zero",
            data: zeros,
            borderColor: 'green',
            pointStyle: 'triangle',
            pointRadius: 0,
            pointHoverRadius: 0,
            pointBackgroundColor: function(context) {
              var index = context.dataIndex;
              var value = context.dataset.data[index];
              // @ts-ignore
              return value < -5 || value > 5 ? 'red' : '#3884de';
            }
          }
        ]
      },
      options: {
        plugins:{
          legend:{
            display: false
          }
        },
        aspectRatio:2.5,
        animations: {
          tension: {
            duration: 1500,
            easing: 'linear',
            from: 0.5,
            to: 0.75,
            loop: true
          }
        },

        scales:{
          y: {
            min: min,
            max: max
          }
        }
      },

    });
  }

  public loadData(){
    this.loading = true;
    let url = 'http://localhost:5000/process_data';
    this.httpClient.post<AnalysisResult>(url, this.rawData).subscribe((response) => {
      this.loading = false;
      this.analysisResult = response;
    }, error => {
      this.loading = false;
        Swal.fire({
            title: 'Error!',
            text: 'An error occurred while processing the data',
            icon: 'error',
            confirmButtonText: 'Ok'
        })

    })
  }

  public reset(){
    this.analysisResult = undefined;
    this.resetEvent.emit();
  }




  protected readonly Number = Number;
  protected readonly Object = Object;
}



























