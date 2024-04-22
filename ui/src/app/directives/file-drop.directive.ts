import { Directive, Output, EventEmitter, HostBinding, HostListener } from '@angular/core';

@Directive({
  selector: '[appFileDrop]',
  standalone: true
})
export class FileDropDirective {
  @Output() fileDropped = new EventEmitter<FileList>();
  @HostBinding('style.background') private background = 'rgba(0,0,0,0.2)';

  @HostListener('dragover', ['$event']) public onDragOver(evt: DragEvent): void {
    evt.preventDefault();
    evt.stopPropagation();
    this.background = '#9ecbec';
  }

  @HostListener('dragleave', ['$event']) public onDragLeave(evt: DragEvent): void {
    evt.preventDefault();
    evt.stopPropagation();
    this.background = 'rgba(0,0,0,0.2)';
  }

  @HostListener('drop', ['$event']) public onDrop(evt: DragEvent): void {
    evt.preventDefault();
    evt.stopPropagation();
    this.background = 'rgba(255,106,0,0.2)';
    const files = evt.dataTransfer?.files;
    if (files) {
      this.fileDropped.emit(files);
    }
  }
}
