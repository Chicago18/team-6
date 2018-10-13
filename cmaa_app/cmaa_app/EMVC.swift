//
//  EMVC.swift
//  cmaa_app
//
//  Created by Sarah Koop on 10/13/18.
//  Copyright © 2018 Sarah Koop. All rights reserved.
//

import UIKit

class EMVC: UIViewController {

    @IBAction func submit(_ sender: Any) {
        performSegue(withIdentifier: "home", sender: self)
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
