//
//  EmergencyContact1VC.swift
//  cmaa_app
//
//  Created by Sarah Koop on 10/13/18.
//  Copyright © 2018 Sarah Koop. All rights reserved.
//

import UIKit

class EmergencyContact1VC: UIViewController {

    @IBAction func next(_ sender: Any) {
        performSegue(withIdentifier: "emercontact1", sender: self)
    }
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
