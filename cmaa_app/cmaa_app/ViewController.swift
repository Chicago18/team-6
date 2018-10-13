//
//  ViewController.swift
//  cmaa_app
//
//  Created by Sarah Koop on 10/13/18.
//  Copyright © 2018 Sarah Koop. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    
    @IBAction func parentBtn(_ sender: Any) {
        performSegue(withIdentifier: "signInToParent", sender: self)
    }
    
   
    @IBAction func adminBtn(_ sender: Any) {
          performSegue(withIdentifier: "goToAdmin", sender: self)
    }
    
    @IBAction func signInBtn(_ sender: Any) {
           performSegue(withIdentifier: "signInToStudent", sender: self)
   
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        
        
        // Do any additional setup after loading the view, typically from a nib.
    }


}

