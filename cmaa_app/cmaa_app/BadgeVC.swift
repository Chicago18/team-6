//
//  BadgeVC.swift
//  cmaa_app
//
//  Created by Sarah Koop on 10/13/18.
//  Copyright © 2018 Sarah Koop. All rights reserved.
//

import UIKit

class BadgeVC: UIViewController {

    @IBOutlet weak var img: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
      self.img.image = UIImage(named: "3.jpg")
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
