import { Component, OnInit, ViewChild, ViewEncapsulation } from '@angular/core';
import {
    FormGroup,
    FormsModule,
    NgForm,
    ReactiveFormsModule,
    UntypedFormBuilder,
    UntypedFormGroup,
    Validators,
} from '@angular/forms';
import { MatSelectModule } from '@angular/material/select';
import { MatButtonModule } from '@angular/material/button';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatOptionModule } from '@angular/material/core';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { Router, RouterLink } from '@angular/router';
import { fuseAnimations } from '@fuse/animations';
import { FuseAlertComponent, FuseAlertType } from '@fuse/components/alert';
import { AuthService } from 'app/core/auth/auth.service';
import {provideNativeDateAdapter} from '@angular/material/core';
import {MatDatepickerModule} from '@angular/material/datepicker';

@Component({
    selector: 'example',
    templateUrl: './example.component.html',
    encapsulation: ViewEncapsulation.None,
    animations: fuseAnimations,
    imports: [
    FuseAlertComponent,
    FormsModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatIconModule,
    MatCheckboxModule,
    MatProgressSpinnerModule,
    MatOptionModule,
    MatSelectModule,
    MatDatepickerModule
],
})
export class ExampleComponent implements OnInit {
    @ViewChild('signUpNgForm') signUpNgForm: NgForm;

    alert: { type: FuseAlertType; message: string } = {
        type: 'success',
        message: '',
    };
    signUpForm: UntypedFormGroup;
    showAlert: boolean = false;

    /**
     * Constructor
     */
    constructor(
        private _authService: AuthService,
        private _formBuilder: UntypedFormBuilder,
        private _router: Router
    ) {}

    // -----------------------------------------------------------------------------------------------------
    // @ Lifecycle hooks
    // -----------------------------------------------------------------------------------------------------

    /**
     * On init
     */
    ngOnInit(): void {
        // Create the form
        this.signUpForm = this._formBuilder.group({
            firstName: ['', Validators.required],
            middleName: [''],
            lastName: ['', Validators.required],
            secondlastName:[''],
            email: ['', [Validators.required, Validators.email]],
            gender: ['', Validators.required],
            birthDate: ['', Validators.required],
            address_line: ['Calle 86 # 69h-35', Validators.required],
            address_city: ['Bogota', Validators.required],
            address_country: ['CO', Validators.required],
        });
    }

    // -----------------------------------------------------------------------------------------------------
    // @ Public methods
    // -----------------------------------------------------------------------------------------------------

    /**
     * Sign up
     */
    register(): void {
        // Do nothing if the form is invalid
        if (this.signUpForm.invalid) {
            return;
        }

        // Disable the form
        this.signUpForm.disable();

        // Hide the alert
        this.showAlert = false;

        // Sign up
        this._authService.registerPatient(
          this.convertFormToFHIR()
        ).subscribe({
           next: (response) => {
                // Navigate to the confirmation required page
               // this._router.navigateByUrl('/confirmation-required');
               console.log(response);
            },
           error: (response) => {
                 console.log(response);
                // Re-enable the form
                this.signUpForm.enable();

                // Reset the form
                this.signUpNgForm.resetForm();

                // Set the alert
                this.alert = {
                    type: 'error',
                    message: 'Something went wrong, please try again.',
                };

                // Show the alert
                this.showAlert = true;
            }
       });
    }


    convertFormToFHIR(): any {
        const formValues = this.signUpForm.value;

        return {
            name: [
                {
                    family: formValues.lastName,
                    given: [formValues.firstName, formValues.middleName].filter(name => name) // Elimina valores vacíos
                }
            ],
            gender: formValues.gender.toLowerCase(), // FHIR usa "male" o "female"
            birthDate: formValues.birthDate,
            address: [
                {
                    line: [formValues.address_line],
                    city: formValues.address_city,
                    country: formValues.address_country
                }
            ]
        };
    }


}

